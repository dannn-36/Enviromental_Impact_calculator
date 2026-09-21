"""Clase base del parser de Java (portada de antlr/grammars-v4)."""
import sys
from typing import TextIO

from antlr4 import Parser, TokenStream


class JavaParserBase(Parser):
    # Tokens que la regla `identifier` acepta como nombre (palabras clave
    # contextuales de Java: module, record, var, yield, ...).
    _IDENTIFIER_TOKEN_NAMES = (
        "IDENTIFIER", "MODULE", "OPEN", "REQUIRES", "EXPORTS", "OPENS", "TO",
        "USES", "PROVIDES", "WHEN", "WITH", "TRANSITIVE", "YIELD", "SEALED",
        "PERMITS", "RECORD", "VAR",
    )

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self._identifier_types = {
            getattr(self, name) for name in self._IDENTIFIER_TOKEN_NAMES if hasattr(self, name)
        }

    def DoLastRecordComponent(self) -> bool:
        """En un record, solo el último componente puede ser varargs (`T... x`)."""
        ctx = self._ctx
        if not hasattr(ctx, "recordComponent"):
            return True
        components = ctx.recordComponent()
        for i, component in enumerate(components):
            if component.ELLIPSIS() is not None and i + 1 < len(components):
                return False
        return True

    def IsNotIdentifierAssign(self) -> bool:
        """Distingue `@Anot(valor)` de `@Anot(nombre = valor)`."""
        if self._input.LA(1) not in self._identifier_types:
            return True
        return self._input.LA(2) != self.ASSIGN
