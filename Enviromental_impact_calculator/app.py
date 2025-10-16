# app.py
# ==============================================================
# 🌱 Environmental Impact Analyzer - FastAPI + ANTLR (Real)
# ==============================================================
# Requisitos (antes de ejecutar):
# 1) Generar parsers ANTLR en Python en carpeta `generated/` (ver conversación).
# 2) pip install fastapi uvicorn antlr4-python3-runtime
# 3) Ejecutar: uvicorn app:app --reload
# ==============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import re
import traceback

# ANTLR imports (podrían fallar si no generaste los parsers)
try:
    from antlr4 import InputStream, CommonTokenStream, FileStream, ParseTreeWalker
    # Intentamos cargar algunos generados (excepciones si no existen)
    # No hacemos imports globales de todos; los haré ad-hoc cuando se necesiten.
    ANTLR_AVAILABLE = True
except Exception:
    ANTLR_AVAILABLE = False

app = FastAPI(title="Environmental Impact Analyzer (real)")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    language: str
    code: str

# -------------------------
# Helpers - regex detectors
# -------------------------
def strip_comments_and_strings(code: str, language: str) -> str:
    # Elimina comentarios y literales de cadena para reducir falsos positivos
    if language == "python":
        code = re.sub(r"('''.*?'''|\"\"\".*?\"\"\")", "", code, flags=re.S)
        code = re.sub(r"#.*?$", "", code, flags=re.M)
        code = re.sub(r"(\".*?\"|'.*?')", "", code, flags=re.S)
    else:
        code = re.sub(r"//.*?$", "", code, flags=re.M)
        code = re.sub(r"/\*.*?\*/", "", code, flags=re.S)
        code = re.sub(r"(\".*?\"|'.*?')", "", code, flags=re.S)
    return code

def detect_functions_regex(code: str, language: str):
    funcs = []
    src = strip_comments_and_strings(code, language)
    if language == "python":
        pattern = re.compile(r'^\s*def\s+([A-Za-z_]\w*)\s*\([^)]*\)\s*:\s*(?:\n(?:[ \t]+.+))+', re.M)
        for m in pattern.finditer(src):
            name = m.group(1)
            full = m.group(0)
            # quitar la línea de la firma (evita falsos positivos de recursión)
            nl = full.find("\n")
            body_only = full[nl+1:] if nl != -1 else ""
            funcs.append((name, body_only))
    elif language in ("c", "c#", "java", "csharp"):
        pattern = re.compile(r'([A-Za-z_][\w<>:\s\*]*?)\s+([A-Za-z_]\w*)\s*\([^;{)]*\)\s*\{', re.M)
        for m in pattern.finditer(src):
            name = m.group(2)
            brace_idx = src.find('{', m.end() - 1)
            if brace_idx == -1:
                continue
            depth = 0
            i = brace_idx
            n = len(src)
            while i < n:
                ch = src[i]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        # solo el cuerpo interno, sin la firma ni la llave de apertura
                        body_only = src[brace_idx+1:i]
                        funcs.append((name, body_only))
                        break
                i += 1
    elif language == "go":
        pattern = re.compile(r'func\s+(?:\([^\)]*\)\s*)?([A-Za-z_]\w*)\s*\([^)]*\)\s*\{', re.M)
        for m in pattern.finditer(src):
            name = m.group(1)
            brace_idx = src.find('{', m.end()-1)
            if brace_idx == -1:
                continue
            depth = 0
            i = brace_idx
            n = len(src)
            while i < n:
                ch = src[i]
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        body_only = src[brace_idx+1:i]
                        funcs.append((name, body_only))
                        break
                i += 1
    return funcs

def detect_loops_regex(code: str, language: str):
    src = strip_comments_and_strings(code, language)
    if language == "python":
        return len(re.findall(r'^\s*(for|while)\b', src, re.M))
    elif language == "go":
        return len(re.findall(r'\bfor\b', src))
    else:
        return len(re.findall(r'\b(for|while|foreach)\b', src))

def detect_assignments_regex(code: str, language: str):
    src = strip_comments_and_strings(code, language)
    if language == "go":
        colon = len(re.findall(r':=', src))
        single = len(re.findall(r'(?<![:!<>=+\-*/%&|^])=(?![=~>])', src))
        return colon + single
    else:
        return len(re.findall(r'(?<![!<>=+\-*/%&|^:])=(?![=~>])', src))

# -------------------------
# Analyzer "real" that uses ANTLR if available
# -------------------------
class RealAnalyzer:
    def __init__(self, language: str):
        self.lang = language.lower()

    def parse_with_antlr(self, code: str):
        """
        Intenta parsear con ANTLR si los módulos generados existen.
        Retorna (success: bool, msg_or_tree)
        """
        if not ANTLR_AVAILABLE:
            return False, "antlr4 runtime not available"

        try:
            # import dinamicamente los módulos generados por lenguaje
            if self.lang == "python":
                from generated.Python3Lexer import Python3Lexer
                from generated.Python3Parser import Python3Parser
                input_stream = InputStream(code)
                lexer = Python3Lexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = Python3Parser(tokens)
                tree = parser.file_input()
                return True, tree
            elif self.lang in ("c",):
                from generated.CLexer import CLexer
                from generated.CParser import CParser
                input_stream = InputStream(code)
                lexer = CLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = CParser(tokens)
                tree = parser.compilationUnit()
                return True, tree
            elif self.lang in ("java",):
                try:
                    from generated.JavaLexer import JavaLexer
                    from generated.JavaParser import JavaParser
                except Exception:
                    from generated.Java20Lexer import Java20Lexer as JavaLexer
                    from generated.Java20Parser import Java20Parser as JavaParser
                input_stream = InputStream(code)
                lexer = JavaLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = JavaParser(tokens)
                tree = parser.compilationUnit()
                return True, tree
            elif self.lang in ("c#", "csharp"):
                from generated.CSharpLexer import CSharpLexer
                from generated.CSharpParser import CSharpParser
                input_stream = InputStream(code)
                lexer = CSharpLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = CSharpParser(tokens)
                tree = parser.compilation_unit()
                return True, tree
            elif self.lang == "go":
                from generated.GoLexer import GoLexer
                from generated.GoParser import GoParser
                input_stream = InputStream(code)
                lexer = GoLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser = GoParser(tokens)
                tree = parser.sourceFile()
                return True, tree
            else:
                return False, f"language {self.lang} not supported for ANTLR parse"
        except Exception as e:
            # devuelve el stack para diagnóstico
            return False, f"antlr parse error: {e}\n{traceback.format_exc()}"

    def analyze(self, code: str):
        parsed, parse_info = self.parse_with_antlr(code)

        loops = detect_loops_regex(code, self.lang)
        functions = detect_functions_regex(code, self.lang)
        assignments = detect_assignments_regex(code, self.lang)

        func_count = len(functions)

        # recursión: buscar name( SOLO dentro del cuerpo (sin la firma)
        recursion_count = 0
        recursive_functions = []
        for name, body_only in functions:
            # nombre de función llamado como llamada (no parte de identificador mayor)
            if re.search(r'(?<!\w)' + re.escape(name) + r'\s*\(', body_only):
                recursion_count += 1
                recursive_functions.append(name)

        metrics = {
            "parsed_with_antlr": bool(parsed),
            "parse_info": str(parse_info) if not parsed else "parsed ok",
            "loops": loops,
            "functions": func_count,
            "assignments": assignments,
            "recursive_functions_count": recursion_count,
            "recursive_functions": recursive_functions
        }
        return metrics

# -------------------------
# Scoring
# -------------------------
def calculate_environmental_score(metrics: dict) -> float:
    loops = metrics.get("loops", 0)
    assignments = metrics.get("assignments", 0)
    recursions = metrics.get("recursive_functions_count", 0)
    # fórmula simple y explicada:
    score = 100 - (loops * 6 + assignments * 1.5 + recursions * 10)
    score = max(0, min(100, score))
    return round(score, 2)

def interpret_score(score: float) -> str:
    if score >= 80:
        return "Excelente eficiencia ambiental 🌿"
    if score >= 60:
        return "Buena eficiencia 🍃"
    if score >= 40:
        return "Moderada 🌱"
    return "Impacto alto ⚠️"

# -------------------------
# API endpoint
# -------------------------
@app.post("/analyze")
def analyze_code(req: CodeRequest):
    lang = req.language.strip().lower()
    code = req.code

    supported = {"python", "c", "java", "c#", "csharp", "go"}
    if lang not in supported:
        raise HTTPException(status_code=400, detail=f"Lenguaje no soportado: {lang}")

    analyzer = RealAnalyzer(lang)
    metrics = analyzer.analyze(code)
    score = calculate_environmental_score(metrics)
    return {
        "language": lang,
        "metrics": metrics,
        "eco_score": score,
        "interpretation": interpret_score(score)
    }

# -------------------------
# Root info
# -------------------------
@app.get("/")
def root():
    info = {
        "message": "Environmental Impact Analyzer (real). Use POST /analyze {language, code}",
        "note": "Asegúrate de generar los parsers ANTLR en generated/ si quieres parsing sintáctico real."
    }
    return info

# ==============================================================
# Fin
# ==============================================================
