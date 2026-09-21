"""Clase base del parser de Python 3 (portada de antlr/grammars-v4).

Los predicados `CannotBePlusMinus` y `CannotBeDotLpEq` existen para que otros
lenguajes destino puedan desambiguar patrones de `match`; en grammars-v4 todas
las implementaciones devuelven True.
"""
import sys
from typing import TextIO

from antlr4 import Parser, TokenStream


class Python3ParserBase(Parser):
    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def CannotBePlusMinus(self) -> bool:
        return True

    def CannotBeDotLpEq(self) -> bool:
        return True
