"""Clase base del parser de C# (portada de antlr/grammars-v4)."""
import sys
from typing import TextIO

from antlr4 import Parser, TokenStream


class CSharpParserBase(Parser):
    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def IsLocalVariableDeclaration(self) -> bool:
        """`var a = 1, b = 2;` no es válido en C#: con `var` solo se permite un declarador."""
        ctx = self._ctx
        if not hasattr(ctx, "local_variable_type"):
            return True
        local_type = ctx.local_variable_type()
        if local_type is None:
            return True
        return local_type.getText() != "var"
