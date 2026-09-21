"""Clase base del lexer de C# (portada de antlr/grammars-v4).

Gestiona los strings interpolados (`$"hola {nombre}"`, `$@"..."`): hay que
llevar la cuenta de las llaves abiertas dentro de cada interpolación para saber
cuándo se vuelve al modo "texto del string".
"""
import sys
from typing import TextIO

from antlr4 import InputStream, Lexer, Token


class CSharpLexerBase(Lexer):
    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.interpolatedStringLevel = 0
        self.interpolatedVerbatiums = []
        self.curlyLevels = []
        self.verbatium = False

    def OnInterpolatedRegularStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(False)
        self.verbatium = False

    def OnInterpolatedVerbatiumStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(True)
        self.verbatium = True

    def OnOpenBrace(self):
        if self.interpolatedStringLevel > 0 and self.curlyLevels:
            self.curlyLevels[-1] += 1

    def OnCloseBrace(self):
        if self.interpolatedStringLevel > 0 and self.curlyLevels:
            self.curlyLevels[-1] -= 1
            if self.curlyLevels[-1] == 0:
                self.curlyLevels.pop()
                self.skip()
                self.popMode()

    def OnColon(self):
        if self.interpolatedStringLevel > 0:
            ind = 1
            switch_to_format_string = True
            while True:
                la = self._input.LA(ind)
                if la == Token.EOF or la == ord("}"):
                    break
                if la in (ord(":"), ord(")")):
                    switch_to_format_string = False
                    break
                ind += 1
            if switch_to_format_string:
                self.mode(self.INTERPOLATION_FORMAT)

    def OpenBraceInside(self):
        self.curlyLevels.append(1)

    def OnDoubleQuoteInside(self):
        self.interpolatedStringLevel -= 1
        if self.interpolatedVerbatiums:
            self.interpolatedVerbatiums.pop()
        self.verbatium = self.interpolatedVerbatiums[-1] if self.interpolatedVerbatiums else False

    def OnCloseBraceInside(self):
        if self.curlyLevels:
            self.curlyLevels.pop()

    def IsRegularCharInside(self) -> bool:
        return not self.verbatium

    def IsVerbatiumDoubleQuoteInside(self) -> bool:
        return self.verbatium
