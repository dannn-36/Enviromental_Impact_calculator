# ==============================================================
# 🌱 Environmental Impact Analyzer - FastAPI + ANTLR
# ==============================================================
# Ejecutar (desde esta carpeta):
#     pip install -r requirements.txt
#     uvicorn app:app --reload
# y abrir http://localhost:8000
# ==============================================================
import os
import sys
import threading
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyzer import LANGUAGES, UnsupportedLanguage, analyze  # noqa: E402

MAX_CODE_CHARS = 300_000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND = os.path.join(BASE_DIR, "frontend", "index.html")
EXAMPLES_DIR = os.path.join(BASE_DIR, "examples")

WARMUP_SNIPPETS = {
    "python": "def f(x):\n    return x\n",
    "c": "int f(int x) { return x; }\n",
    "java": "class A { int f(int x) { return x; } }\n",
    "go": "package main\nfunc f(x int) int { return x }\n",
    "csharp": "class A { int F(int x) { return x; } }\n",
}


def _warm_up():
    # La primera vez que se usa cada parser, el runtime de ANTLR deserializa su
    # ATN y construye cachés (1-3 s por lenguaje). Se hace al arrancar para que
    # la primera petición del usuario sea rápida.
    for language, code in WARMUP_SNIPPETS.items():
        analyze(code, language)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    threading.Thread(target=_warm_up, daemon=True).start()
    yield


app = FastAPI(
    title="Environmental Impact Analyzer",
    description="Análisis estático (ANTLR) del impacto ambiental de algoritmos en "
                "Python, C, Java, Go y C#.",
    version="2.0.0",
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    language: str = Field(..., examples=["python"])
    code: str = Field(..., examples=["def f(n):\n    return n\n"])


@app.post("/analyze")
def analyze_code(req: CodeRequest):
    if len(req.code) > MAX_CODE_CHARS:
        raise HTTPException(status_code=413,
                            detail=f"El código supera el máximo de {MAX_CODE_CHARS} caracteres")
    try:
        return analyze(req.code, req.language)
    except UnsupportedLanguage:
        supported = ", ".join(LANGUAGES)
        raise HTTPException(status_code=400,
                            detail=f"Lenguaje no soportado: {req.language}. Soportados: {supported}")


@app.get("/languages")
def languages():
    return [
        {
            "key": spec.key,
            "name": spec.display_name,
            "aliases": list(spec.aliases),
            "extensions": list(spec.extensions),
            "energy_factor": spec.energy_factor,
        }
        for spec in LANGUAGES.values()
    ]


@app.get("/examples")
def examples():
    """Código de ejemplo (mismos algoritmos en cada lenguaje) para probar la app."""
    result = {}
    for filename in sorted(os.listdir(EXAMPLES_DIR)):
        ext = os.path.splitext(filename)[1].lower()
        for spec in LANGUAGES.values():
            if ext in spec.extensions and spec.key not in result:
                with open(os.path.join(EXAMPLES_DIR, filename), encoding="utf-8") as f:
                    result[spec.key] = {"filename": filename, "code": f.read()}
    return result


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse(FRONTEND)
