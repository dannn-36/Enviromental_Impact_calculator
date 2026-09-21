"""Análisis estático real sobre el árbol sintáctico generado por ANTLR.

Flujo:
  1. `parse()` tokeniza y parsea el código con la gramática del lenguaje,
     recogiendo los errores de sintaxis (no se imprimen por consola).
  2. `TreeAnalyzer` recorre el árbol una sola vez y cuenta, por función:
     bucles (y su anidamiento), puntos de decisión, asignaciones, operadores,
     llamadas y reservas de memoria.
  3. Con las llamadas se construye un grafo de llamadas que permite detectar
     recursión directa y mutua, y estimar la complejidad temporal de cada
     función teniendo en cuenta lo que hacen las funciones a las que llama.
"""
import importlib
import itertools
import re
import threading
import time
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Dict, List, Optional, Set

from antlr4 import CommonTokenStream, InputStream, ParserRuleContext, Token
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import BailErrorStrategy, DefaultErrorStrategy
from antlr4.error.Errors import ParseCancellationException
from antlr4.tree.Tree import TerminalNode

from .languages import LanguageSpec

# Palabras clave (tokens que no son identificadores) que abren un bucle o una
# decisión. Se reconocen por su texto, que es igual en los cinco lenguajes.
LOOP_KEYWORDS = frozenset({"for", "foreach", "while", "do"})
BRANCH_KEYWORDS = frozenset({"if", "elif", "case", "catch", "except"})
CONDITIONAL_KEYWORDS = frozenset({"if", "else", "elif", "?", "switch", "match", "select"})
LOGICAL_OPERATORS = frozenset({"&&", "||", "and", "or"})

ASSIGNMENT_OPERATORS = frozenset({
    "=", ":=", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "<<=", ">>=", ">>>=",
    "**=", "//=", "@=", "&^=", "??=",
})
INCREMENT_OPERATORS = frozenset({"++", "--"})
ARITHMETIC_OPERATORS = frozenset({
    "+", "-", "*", "/", "%", "**", "//", "@", "<<", ">>", ">>>", "&", "|", "^", "~", "&^",
    "!", "not", "==", "!=", "<", ">", "<=", ">=", "is", "in", "??",
}) | LOGICAL_OPERATORS

# Reglas de la gramática de Python cuyo nombre no contiene "expr" pero que son
# expresiones (en el resto de gramáticas todas contienen "expr").
PYTHON_EXPRESSION_RULES = frozenset({
    "TermContext", "FactorContext", "PowerContext", "ComparisonContext", "Comp_opContext",
    "Not_testContext", "And_testContext", "Or_testContext",
})

NOT_A_CALLEE = frozenset({
    "this", "super", "base", "new", "typeof", "sizeof", "nameof", "default", "return",
    "if", "while", "for", "switch", "catch", "checked", "unchecked", "await",
})
IDENTIFIER_RE = re.compile(r"^[A-Za-z_]\w*$")
HALVING_RE = re.compile(r"/\s*2\b|//\s*2\b|>>\s*1\b|\bmid\b|\bmiddle\b|\bhalf\b|\bmedio\b|\bmitad\b",
                        re.I)

MODULE_SCOPE = "<global>"
ASSUMED_ITERATIONS = 10  # iteraciones supuestas por bucle al estimar operaciones ejecutadas

_locks: Dict[str, threading.Lock] = {}


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------
class CollectingErrorListener(ErrorListener):
    def __init__(self, source: str):
        self.source = source
        self.errors: List[dict] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if len(self.errors) < 50:
            self.errors.append({"source": self.source, "line": line, "column": column, "message": msg})


@lru_cache(maxsize=None)
def _load(module: str, cls: str):
    return getattr(importlib.import_module(f"generated.{module}"), cls)


@dataclass
class ParseResult:
    tree: ParserRuleContext
    tokens: CommonTokenStream
    source: str
    errors: List[dict]
    elapsed_ms: float
    prediction_mode: str


def parse(code: str, spec: LanguageSpec) -> ParseResult:
    lexer_cls = _load(*spec.lexer)
    parser_cls = _load(*spec.parser)
    if spec.ensure_trailing_newline and not code.endswith("\n"):
        code += "\n"

    lock = _locks.setdefault(spec.key, threading.Lock())
    with lock:  # la caché de DFAs del runtime de ANTLR no es thread-safe
        start = time.perf_counter()
        lexer_errors = CollectingErrorListener("lexer")
        lexer = lexer_cls(InputStream(code))
        lexer.removeErrorListeners()
        lexer.addErrorListener(lexer_errors)
        tokens = CommonTokenStream(lexer)
        tokens.fill()

        parser = parser_cls(tokens)
        parser.removeErrorListeners()
        entry = getattr(parser, spec.entry_rule)

        # Fase 1: SLL (rápido). Si falla, puede ser un falso negativo de SLL,
        # así que se repite con LL completo, que además da buenos mensajes.
        parser._interp.predictionMode = PredictionMode.SLL
        parser._errHandler = BailErrorStrategy()
        mode = "SLL"
        parser_errors = CollectingErrorListener("parser")
        try:
            tree = entry()
        except ParseCancellationException:
            tokens.seek(0)
            parser.reset()
            parser._interp.predictionMode = PredictionMode.LL
            parser._errHandler = DefaultErrorStrategy()
            parser.addErrorListener(parser_errors)
            tree = entry()
            mode = "LL"
        elapsed = (time.perf_counter() - start) * 1000

    return ParseResult(tree, tokens, code, lexer_errors.errors + parser_errors.errors,
                       round(elapsed, 1), mode)


# ---------------------------------------------------------------------------
# Recorrido del árbol
# ---------------------------------------------------------------------------
@dataclass
class CallSite:
    name: Optional[str]
    loop_depth: int          # profundidad de bucles relativa a la función
    token_index: int
    node: object


@dataclass
class FunctionInfo:
    name: str
    line: int
    end_line: int
    ctx: Optional[ParserRuleContext] = None
    loops: int = 0
    max_loop_depth: int = 0
    decisions: int = 0
    branches: int = 0
    assignments: int = 0
    operators: int = 0
    allocations: int = 0
    allocations_in_loops: int = 0
    estimated_operations: int = 0
    calls: List[CallSite] = field(default_factory=list)
    # Rellenados en la fase del grafo de llamadas
    recursive: bool = False
    recursion_kind: Optional[str] = None     # "directa" | "mutua"
    recursion_branching: int = 0
    halving: bool = False
    effective_loop_depth: int = 0
    complexity: Optional["Complexity"] = None

    @property
    def cyclomatic(self) -> int:
        return 1 + self.decisions


@dataclass(frozen=True, order=True)
class Complexity:
    """Orden de complejidad O(n^poly · log^log n), o exponencial."""
    exponential: bool = False
    poly: int = 0
    log: int = 0

    def label(self) -> str:
        if self.exponential:
            return "O(2ⁿ)"
        sup = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
        parts = []
        if self.poly == 1:
            parts.append("n")
        elif self.poly > 1:
            parts.append("n" + str(self.poly).translate(sup))
        if self.log:
            parts.append("log n")
        return f"O({' '.join(parts) or '1'})"


class TreeAnalyzer:
    def __init__(self, spec: LanguageSpec, parse_result: ParseResult):
        self.spec = spec
        self.tree = parse_result.tree
        self.tokens = parse_result.tokens
        self.source = parse_result.source
        lexer_cls = _load(*spec.lexer)
        self.identifier_types = frozenset(
            getattr(lexer_cls, name) for name in spec.identifier_tokens if hasattr(lexer_cls, name))
        self.module = FunctionInfo(MODULE_SCOPE, 1, 1)
        self.functions: List[FunctionInfo] = []

    # -- utilidades ---------------------------------------------------------
    def _is_keyword(self, terminal: TerminalNode) -> bool:
        return terminal.symbol.type not in self.identifier_types

    def _is_loop(self, ctx: ParserRuleContext) -> bool:
        for child in ctx.children or ():
            if (isinstance(child, TerminalNode) and child.getText() in LOOP_KEYWORDS
                    and self._is_keyword(child)):
                return True
        return False

    def _is_conditional(self, ctx: ParserRuleContext) -> bool:
        for child in ctx.children or ():
            if (isinstance(child, TerminalNode) and child.getText() in CONDITIONAL_KEYWORDS
                    and self._is_keyword(child)):
                return True
        return False

    def _is_return(self, ctx: ParserRuleContext) -> bool:
        first = ctx.children[0] if ctx.children else None
        return isinstance(first, TerminalNode) and first.getText() == "return"

    @staticmethod
    def _is_expression_parent(ctx) -> bool:
        name = type(ctx).__name__
        return ("expr" in name.lower() or name in PYTHON_EXPRESSION_RULES) and \
            name != "Bracket_expressionContext"

    def _previous_token(self, node) -> Optional[Token]:
        index = node.symbol.tokenIndex if isinstance(node, TerminalNode) else node.start.tokenIndex
        index -= 1
        while index >= 0:
            token = self.tokens.get(index)
            if token.channel == Token.DEFAULT_CHANNEL:
                return token
            index -= 1
        return None

    def _callee_name(self, node) -> Optional[str]:
        token = self._previous_token(node)
        if token is not None and IDENTIFIER_RE.match(token.text) and token.text not in NOT_A_CALLEE:
            return token.text
        return None

    def _end_line(self, ctx) -> int:
        # En Python el último token de una función es un DEDENT, que se emite
        # después de las líneas en blanco; se busca el último token con texto.
        if ctx.stop is None:
            return ctx.start.line
        index = ctx.stop.tokenIndex
        while index > ctx.start.tokenIndex:
            token = self.tokens.get(index)
            if token.channel == Token.DEFAULT_CHANNEL and token.text and token.text.strip():
                return token.line
            index -= 1
        return ctx.start.line

    def _source_text(self, ctx) -> str:
        if ctx is None or ctx.start is None or ctx.stop is None:
            return ""
        return self.source[ctx.start.start:ctx.stop.stop + 1]

    def _function_name(self, ctx) -> Optional[str]:
        extractor = self.spec.function_rules.get(type(ctx).__name__)
        if extractor is None:
            return None
        try:
            return extractor(ctx, self.identifier_types)
        except (AttributeError, TypeError):
            return None  # nodo incompleto por un error de sintaxis

    # -- recorrido ----------------------------------------------------------
    def run(self):
        func_stack: List[FunctionInfo] = [self.module]
        loop_depths: List[int] = [0]   # profundidad de bucles, una entrada por función abierta
        # Pila explícita (los árboles de ANTLR son muy profundos para recursión)
        stack = [(self.tree, False, False, False)]
        while stack:
            node, exiting, opened_function, opened_loop = stack.pop()
            if exiting:
                if opened_loop:
                    loop_depths[-1] -= 1
                if opened_function:
                    func_stack.pop()
                    loop_depths.pop()
                continue

            current = func_stack[-1]
            depth = loop_depths[-1]

            if isinstance(node, TerminalNode):
                if self.spec.is_call(node):
                    self._record_call(node, current, depth)
                self._visit_terminal(node, current, depth)
                continue

            pushed_function = pushed_loop = False
            name = self._function_name(node)
            if name:
                info = FunctionInfo(name, node.start.line, self._end_line(node), node)
                self.functions.append(info)
                func_stack.append(info)
                loop_depths.append(0)
                current, depth, pushed_function = info, 0, True

            if self.spec.is_call(node):
                self._record_call(node, current, depth)

            if self._is_loop(node):
                depth += 1
                loop_depths[-1] = depth
                current.loops += 1
                current.decisions += 1
                current.max_loop_depth = max(current.max_loop_depth, depth)
                pushed_loop = True

            stack.append((node, True, pushed_function, pushed_loop))
            for child in reversed(node.children or ()):
                stack.append((child, False, False, False))

    def _record_call(self, node, current: FunctionInfo, depth: int):
        name = self._callee_name(node)
        token_index = node.symbol.tokenIndex if isinstance(node, TerminalNode) else node.start.tokenIndex
        current.calls.append(CallSite(name, depth, token_index, node))
        current.estimated_operations += ASSUMED_ITERATIONS ** depth
        if name in self.spec.allocation_calls:
            self._record_allocation(current, depth)

    @staticmethod
    def _record_allocation(current: FunctionInfo, depth: int):
        current.allocations += 1
        if depth:
            current.allocations_in_loops += 1

    def _visit_terminal(self, node: TerminalNode, current: FunctionInfo, depth: int):
        if node.symbol.type == Token.EOF:
            return
        text = node.getText()
        parent = node.parentCtx
        parent_name = type(parent).__name__
        weight = ASSUMED_ITERATIONS ** depth

        if self._is_keyword(node):
            if text in BRANCH_KEYWORDS:
                current.decisions += 1
                current.branches += 1
                return
            if text == "?" and self._is_expression_parent(parent):
                current.decisions += 1
                current.branches += 1
                return
            previous = self._previous_token(node)
            if (text == "new" and "modifier" not in parent_name.lower()
                    and (previous is None or previous.text != "::")):
                self._record_allocation(current, depth)
                current.estimated_operations += weight
                return

        if text in ASSIGNMENT_OPERATORS or (text == ">=" and parent_name == "Right_shift_assignmentContext"):
            if parent_name not in self.spec.assignment_excluded_parents:
                current.assignments += 1
                current.estimated_operations += weight
            return
        if text in INCREMENT_OPERATORS:
            current.assignments += 1
            current.estimated_operations += weight
            return
        if text in ARITHMETIC_OPERATORS and self._is_expression_parent(parent):
            current.operators += 1
            current.estimated_operations += weight
            if text in LOGICAL_OPERATORS or text == "??":
                current.decisions += 1

    # -- grafo de llamadas --------------------------------------------------
    def analyze_call_graph(self):
        by_name: Dict[str, List[FunctionInfo]] = {}
        for f in self.functions:
            by_name.setdefault(f.name, []).append(f)

        graph: Dict[str, Set[str]] = {name: set() for name in by_name}
        for f in self.functions:
            for call in f.calls:
                if call.name in by_name:
                    graph[f.name].add(call.name)

        # Componentes fuertemente conexas (Tarjan): una función es recursiva si
        # se llama a sí misma o forma parte de un ciclo con otras.
        cyclic: Dict[str, str] = {}
        for component in _strongly_connected_components(graph):
            if len(component) > 1:
                for name in component:
                    cyclic[name] = "mutua"
            else:
                (name,) = component
                if name in graph[name]:
                    cyclic[name] = "directa"

        for f in self.functions:
            kind = cyclic.get(f.name)
            if not kind:
                continue
            f.recursive = True
            f.recursion_kind = kind
            self_calls = [c for c in f.calls if c.name == f.name]
            f.recursion_branching = self._max_simultaneous_calls(f, self_calls) if self_calls else 1
            f.halving = bool(HALVING_RE.search(self._source_text(f.ctx)))

        # Profundidad de bucles efectiva: incluye la de las funciones llamadas
        # (una llamada dentro de un bucle a una función con un bucle = 2 niveles).
        memo: Dict[str, int] = {}

        def effective_depth(name: str, visiting: Set[str]) -> int:
            if name in memo:
                return memo[name]
            if name in visiting:
                return 0
            visiting.add(name)
            best = 0
            for f in by_name.get(name, []):
                best = max(best, f.max_loop_depth)
                for call in f.calls:
                    if call.name in by_name and call.name != name:
                        best = max(best, call.loop_depth + effective_depth(call.name, visiting))
            visiting.discard(name)
            memo[name] = best
            return best

        for f in self.functions:
            f.effective_loop_depth = effective_depth(f.name, set())
            f.complexity = estimate_complexity(f)

        module = self.module
        module.effective_loop_depth = module.max_loop_depth
        for call in module.calls:
            if call.name in by_name:
                module.effective_loop_depth = max(
                    module.effective_loop_depth, call.loop_depth + memo.get(call.name, 0))
        module.complexity = estimate_complexity(module)

    def _max_simultaneous_calls(self, f: FunctionInfo, calls: List[CallSite]) -> int:
        """Máximo número de auto-llamadas que pueden ejecutarse en una misma
        invocación. Dos llamadas son excluyentes si están en ramas distintas de
        un if/switch/ternario, o en sentencias `return` distintas."""
        if len(calls) <= 1:
            return len(calls)
        calls = calls[:12]
        paths = [self._branch_path(f, c.node) for c in calls]

        def exclusive(a, b) -> bool:
            (arms_a, ret_a), (arms_b, ret_b) = a, b
            for ctx_id, arm in arms_a.items():
                if ctx_id in arms_b and arms_b[ctx_id] != arm:
                    return True
            return ret_a is not None and ret_b is not None and ret_a != ret_b

        for size in range(len(calls), 1, -1):
            for combo in itertools.combinations(range(len(calls)), size):
                if all(not exclusive(paths[i], paths[j]) for i, j in itertools.combinations(combo, 2)):
                    return size
        return 1

    def _branch_path(self, f: FunctionInfo, node):
        arms: Dict[int, int] = {}
        return_stmt = None
        child, parent = node, node.parentCtx
        while parent is not None and child is not f.ctx:
            if isinstance(parent, ParserRuleContext) and parent.children:
                if self._is_conditional(parent):
                    arms[id(parent)] = parent.children.index(child)
                if return_stmt is None and self._is_return(parent):
                    return_stmt = id(parent)
            child, parent = parent, parent.parentCtx
        return arms, return_stmt


def _strongly_connected_components(graph: Dict[str, Set[str]]):
    index_of: Dict[str, int] = {}
    low: Dict[str, int] = {}
    on_stack: Set[str] = set()
    stack: List[str] = []
    counter = itertools.count()
    components = []

    for root in graph:
        if root in index_of:
            continue
        work = [(root, iter(sorted(graph[root])))]
        index_of[root] = low[root] = next(counter)
        stack.append(root)
        on_stack.add(root)
        while work:
            node, neighbours = work[-1]
            advanced = False
            for nxt in neighbours:
                if nxt not in index_of:
                    index_of[nxt] = low[nxt] = next(counter)
                    stack.append(nxt)
                    on_stack.add(nxt)
                    work.append((nxt, iter(sorted(graph[nxt]))))
                    advanced = True
                    break
                if nxt in on_stack:
                    low[node] = min(low[node], index_of[nxt])
            if advanced:
                continue
            work.pop()
            if work:
                low[work[-1][0]] = min(low[work[-1][0]], low[node])
            if low[node] == index_of[node]:
                component = set()
                while True:
                    member = stack.pop()
                    on_stack.discard(member)
                    component.add(member)
                    if member == node:
                        break
                components.append(component)
    return components


def estimate_complexity(f: FunctionInfo) -> Complexity:
    """Estimación heurística de la complejidad temporal.

    D = profundidad efectiva de bucles, b = auto-llamadas por invocación,
    h = los argumentos dividen el problema (mid, n/2, >>1, ...).
      * sin recursión:             O(n^D)
      * b = 1, h:                  O(log n) si D = 0, si no O(n^D)
      * b = 1, sin h:              O(n^(D+1))       (recursión lineal)
      * b ≥ 2, h:                  O(n) si D = 0, O(n log n) si D = 1, si no O(n^D)
      * b ≥ 2, sin h, D = 0:       O(2^n)           (fibonacci, hanoi, subconjuntos)
      * b ≥ 2, sin h, D ≥ 1:       O(n log n) / O(n^D)  (quicksort y similares)
    """
    d = f.effective_loop_depth
    if not f.recursive:
        return Complexity(poly=d)
    b = max(1, f.recursion_branching)
    if b == 1:
        if f.halving:
            return Complexity(poly=d, log=0) if d else Complexity(log=1)
        return Complexity(poly=d + 1)
    if f.halving or d >= 1:
        if d == 0:
            return Complexity(poly=1)
        if d == 1:
            return Complexity(poly=1, log=1)
        return Complexity(poly=d)
    return Complexity(exponential=True)


def logical_lines(tokens: CommonTokenStream) -> int:
    lines = set()
    for token in tokens.tokens:
        if token.channel == Token.DEFAULT_CHANNEL and token.type != Token.EOF and token.text.strip():
            lines.add(token.line)
    return len(lines)
