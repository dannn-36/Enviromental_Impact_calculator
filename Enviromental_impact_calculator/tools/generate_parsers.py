"""Genera los lexers/parsers de Python a partir de las gramáticas ANTLR.

Uso (desde la carpeta Enviromental_impact_calculator/):

    python tools/generate_parsers.py

Requisitos: Java 11+ en el PATH. El .jar de ANTLR ya está en el repositorio.

Qué hace:
  1. Copia las gramáticas de grammars/ a un directorio temporal cambiando
     `this.` por `self.` en las acciones y predicados. Las gramáticas de
     grammars-v4 están escritas de forma "neutral" con `this.` (válido en
     Java/C#/JS); para el target Python hay que usar `self.`. Sin este paso el
     código generado lanza `NameError: name 'this' is not defined`.
  2. Ejecuta ANTLR 4.13.2 con -Dlanguage=Python3 y deja el resultado en generated/.
  3. Copia las clases base escritas a mano (grammars/base/*.py) a generated/.
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GRAMMARS = ROOT / "grammars"
BASES = GRAMMARS / "base"
OUT = ROOT / "generated"
JAR = ROOT / "antlr-4.13.2-complete.jar"

# Cada entrada es una invocación de ANTLR; el lexer siempre va antes que el
# parser para que exista el .tokens que usa `tokenVocab`.
GRAMMAR_SETS = [
    ["C.g4"],
    ["JavaLexer.g4", "JavaParser.g4"],
    ["Python3Lexer.g4", "Python3Parser.g4"],
    ["GoLexer.g4", "GoParser.g4"],
    ["CSharpLexer.g4", "CSharpParser.g4"],
]


def main() -> int:
    if not JAR.exists():
        print(f"No se encuentra {JAR}", file=sys.stderr)
        return 1
    if shutil.which("java") is None:
        print("Hace falta Java (11 o superior) en el PATH para ejecutar ANTLR.", file=sys.stderr)
        return 1

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        for g4 in GRAMMARS.glob("*.g4"):
            text = g4.read_text(encoding="utf-8")
            (tmp_dir / g4.name).write_text(re.sub(r"\bthis\.", "self.", text), encoding="utf-8")

        for files in GRAMMAR_SETS:
            cmd = [
                "java", "-jar", str(JAR),
                "-Dlanguage=Python3", "-no-listener", "-no-visitor",
                "-Xexact-output-dir", "-o", str(OUT), "-lib", str(tmp_dir),
                *[str(tmp_dir / f) for f in files],
            ]
            print("ANTLR:", " ".join(files))
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0 or "error(" in result.stderr:
                print(result.stdout, result.stderr, file=sys.stderr)
                return result.returncode or 1

    for base in BASES.glob("*.py"):
        shutil.copy(base, OUT / base.name)
    (OUT / "__init__.py").write_text(
        '"""Código generado por tools/generate_parsers.py. No editar a mano."""\n',
        encoding="utf-8",
    )
    print(f"Parsers generados en {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
