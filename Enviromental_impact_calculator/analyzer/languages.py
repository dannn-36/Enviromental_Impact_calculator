"""Descripción de cada lenguaje soportado.

El analizador (core.py) recorre el árbol sintáctico de ANTLR de forma genérica.
Lo único que cambia entre lenguajes es:
  * qué lexer/parser usar y cuál es la regla inicial,
  * qué nodos del árbol son definiciones de función y cómo sacar su nombre,
  * qué nodos son llamadas a función,
  * qué asignaciones no cuentan (valores por defecto de parámetros, etc.),
  * qué llamadas reservan memoria (malloc, make, ...).

Los nodos se identifican por el nombre de su clase de contexto generada por
ANTLR (p. ej. `FuncdefContext`), así este módulo no necesita importar los
parsers generados.
"""
from dataclasses import dataclass, field
from typing import Callable, Dict, FrozenSet, Optional, Tuple

from antlr4 import ParserRuleContext
from antlr4.tree.Tree import TerminalNode


def terminals(node):
    """Todos los tokens (hojas) de un subárbol, en orden."""
    stack = [node]
    while stack:
        current = stack.pop()
        if isinstance(current, TerminalNode):
            yield current
        elif current.children:
            stack.extend(reversed(current.children))


def first_identifier(node, identifier_types) -> Optional[str]:
    for t in terminals(node):
        if t.symbol.type in identifier_types:
            return t.getText()
    return None


def last_identifier(node, identifier_types) -> Optional[str]:
    name = None
    for t in terminals(node):
        if t.symbol.type in identifier_types:
            name = t.getText()
    return name


def child_text(ctx, index: int) -> Optional[str]:
    if ctx.children and len(ctx.children) > index:
        return ctx.children[index].getText()
    return None


# ---------------------------------------------------------------------------
# Extractores de nombre de función. Devuelven None si el nodo no es una
# función con cuerpo (p. ej. un método abstracto o de interfaz sin código).
# ---------------------------------------------------------------------------
NameExtractor = Callable[[ParserRuleContext, FrozenSet[int]], Optional[str]]


def _python_funcdef(ctx, ids):
    return ctx.name().getText()


def _c_function(ctx, ids):
    return first_identifier(ctx.declarator(), ids)


def _java_method(ctx, ids):
    body = ctx.methodBody()
    if body is None or body.block() is None:
        return None
    return ctx.identifier().getText()


def _java_constructor(ctx, ids):
    return ctx.identifier().getText()


def _go_function(ctx, ids):
    if ctx.block() is None:
        return None
    return ctx.IDENTIFIER().getText()


def _cs_method(ctx, ids):
    body = ctx.method_body()
    if body is not None and body.block() is None:
        return None  # método abstracto / de interfaz / extern
    return last_identifier(ctx.method_member_name(), ids)


def _cs_constructor(ctx, ids):
    return ctx.identifier().getText()


def _cs_local_function(ctx, ids):
    return ctx.local_function_header().identifier().getText()


def _cs_destructor(ctx, ids):
    return "~" + ctx.identifier().getText()


def _cs_operator(ctx, ids):
    return "operator " + ctx.overloadable_operator().getText()


# ---------------------------------------------------------------------------
# Detectores de llamada. Reciben un nodo del árbol y dicen si es el "(" de una
# llamada a función. El nombre de la función llamada se obtiene después como
# el identificador inmediatamente anterior en el flujo de tokens.
# ---------------------------------------------------------------------------
def _python_is_call(node):
    return type(node).__name__ == "TrailerContext" and child_text(node, 0) == "("


def _c_is_call(node):
    # En la gramática de C las llamadas son un '(' dentro de postfixExpression
    # que va detrás de otra cosa (y no es el literal compuesto `(tipo){...}`).
    if not isinstance(node, TerminalNode) or node.getText() != "(":
        return False
    parent = node.parentCtx
    if type(parent).__name__ != "PostfixExpressionContext":
        return False
    index = parent.children.index(node)
    return index > 0 and parent.children[index - 1].getText() != "__extension__"


def _java_is_call(node):
    return (type(node).__name__ == "ArgumentsContext"
            and type(node.parentCtx).__name__ == "MethodCallContext")


def _go_is_call(node):
    return (type(node).__name__ == "ArgumentsContext"
            and type(node.parentCtx).__name__ == "PrimaryExprContext")


def _cs_is_call(node):
    return type(node).__name__ == "Method_invocationContext"


@dataclass(frozen=True)
class LanguageSpec:
    key: str
    display_name: str
    lexer: Tuple[str, str]           # (módulo, clase) dentro de generated/
    parser: Tuple[str, str]
    entry_rule: str
    identifier_tokens: Tuple[str, ...]
    function_rules: Dict[str, NameExtractor]
    is_call: Callable[[object], bool]
    assignment_excluded_parents: FrozenSet[str] = frozenset()
    allocation_calls: FrozenSet[str] = frozenset()
    # Consumo energético normalizado (C = 1.00) según Pereira et al.,
    # "Energy Efficiency across Programming Languages", SLE 2017, tabla 4.
    energy_factor: float = 1.0
    extensions: Tuple[str, ...] = ()
    ensure_trailing_newline: bool = False
    aliases: Tuple[str, ...] = field(default=())


LANGUAGES: Dict[str, LanguageSpec] = {
    "python": LanguageSpec(
        key="python",
        display_name="Python",
        lexer=("Python3Lexer", "Python3Lexer"),
        parser=("Python3Parser", "Python3Parser"),
        entry_rule="file_input",
        identifier_tokens=("NAME",),
        function_rules={"FuncdefContext": _python_funcdef},
        is_call=_python_is_call,
        assignment_excluded_parents=frozenset(
            {"ArgumentContext", "TypedargslistContext", "VarargslistContext"}),
        allocation_calls=frozenset(
            {"list", "dict", "set", "tuple", "bytearray", "copy", "deepcopy", "append", "extend"}),
        energy_factor=75.88,
        extensions=(".py",),
        ensure_trailing_newline=True,
        aliases=("py", "python3"),
    ),
    "c": LanguageSpec(
        key="c",
        display_name="C",
        lexer=("CLexer", "CLexer"),
        parser=("CParser", "CParser"),
        entry_rule="compilationUnit",
        identifier_tokens=("Identifier",),
        function_rules={"FunctionDefinitionContext": _c_function},
        is_call=_c_is_call,
        assignment_excluded_parents=frozenset({"EnumeratorContext"}),
        allocation_calls=frozenset({"malloc", "calloc", "realloc", "strdup", "strndup", "alloca"}),
        energy_factor=1.00,
        extensions=(".c", ".h"),
    ),
    "java": LanguageSpec(
        key="java",
        display_name="Java",
        lexer=("JavaLexer", "JavaLexer"),
        parser=("JavaParser", "JavaParser"),
        entry_rule="compilationUnit",
        identifier_tokens=("IDENTIFIER", "MODULE", "OPEN", "REQUIRES", "EXPORTS", "OPENS", "TO",
                           "USES", "PROVIDES", "WHEN", "WITH", "TRANSITIVE", "YIELD", "SEALED",
                           "PERMITS", "RECORD", "VAR"),
        function_rules={
            "MethodDeclarationContext": _java_method,
            "InterfaceCommonBodyDeclarationContext": _java_method,
            "ConstructorDeclarationContext": _java_constructor,
            "CompactConstructorDeclarationContext": _java_constructor,
        },
        is_call=_java_is_call,
        assignment_excluded_parents=frozenset({"ElementValuePairContext"}),
        energy_factor=1.98,
        extensions=(".java",),
    ),
    "go": LanguageSpec(
        key="go",
        display_name="Go",
        lexer=("GoLexer", "GoLexer"),
        parser=("GoParser", "GoParser"),
        entry_rule="sourceFile",
        identifier_tokens=("IDENTIFIER",),
        function_rules={
            "FunctionDeclContext": _go_function,
            "MethodDeclContext": _go_function,
        },
        is_call=_go_is_call,
        allocation_calls=frozenset({"make", "new", "append"}),
        energy_factor=3.23,
        extensions=(".go",),
        ensure_trailing_newline=True,
    ),
    "csharp": LanguageSpec(
        key="csharp",
        display_name="C#",
        lexer=("CSharpLexer", "CSharpLexer"),
        parser=("CSharpParser", "CSharpParser"),
        entry_rule="compilation_unit",
        identifier_tokens=("IDENTIFIER",),
        function_rules={
            "Method_declarationContext": _cs_method,
            "Constructor_declarationContext": _cs_constructor,
            "Local_function_declarationContext": _cs_local_function,
            "Destructor_definitionContext": _cs_destructor,
            "Operator_declarationContext": _cs_operator,
        },
        is_call=_cs_is_call,
        assignment_excluded_parents=frozenset({
            "Fixed_parameterContext", "Arg_declarationContext",
            "Attribute_argumentContext", "Using_alias_directiveContext",
        }),
        energy_factor=3.14,
        extensions=(".cs",),
        aliases=("c#", "cs"),
    ),
}


def resolve_language(name: str) -> Optional[LanguageSpec]:
    key = (name or "").strip().lower()
    if key in LANGUAGES:
        return LANGUAGES[key]
    for spec in LANGUAGES.values():
        if key in spec.aliases:
            return spec
    return None
