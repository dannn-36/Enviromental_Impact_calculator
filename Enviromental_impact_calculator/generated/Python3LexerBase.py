"""Clase base del lexer de Python 3 (portada de antlr/grammars-v4).

Python no delimita bloques con llaves sino con indentación, así que el lexer
tiene que *inventar* tokens INDENT / DEDENT a partir de los espacios al inicio
de cada línea. Las acciones de la gramática (`self.onNewLine()`,
`self.openBrace()`, ...) llaman a estos métodos.
"""
import re
import sys
from typing import TextIO

from antlr4 import InputStream, Lexer, Token
from antlr4.Token import CommonToken


class Python3LexerBase(Lexer):
    NEW_LINE_PATTERN = re.compile(r"[^\r\n\f]+")
    SPACES_PATTERN = re.compile(r"[\r\n\f]+")

    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.tokens = []    # cola de tokens pendientes de entregar
        self.indents = []   # pila de niveles de indentación abiertos
        self.opened = 0     # paréntesis/corchetes/llaves abiertos

    def reset(self):
        self.tokens = []
        self.indents = []
        self.opened = 0
        super().reset()

    def emitToken(self, token):
        self._token = token
        self.tokens.append(token)

    def nextToken(self):
        # Al llegar al EOF hay que cerrar todos los bloques abiertos.
        if self._input.LA(1) == Token.EOF and self.indents:
            self.tokens = [t for t in self.tokens if t.type != Token.EOF]
            self.emitToken(self.commonToken(self.NEWLINE, "\n"))
            while self.indents:
                self.emitToken(self.createDedent())
                self.indents.pop()
            self.emitToken(self.commonToken(Token.EOF, "<EOF>"))

        next_ = super().nextToken()
        return next_ if not self.tokens else self.tokens.pop(0)

    def createDedent(self):
        return self.commonToken(self.DEDENT, "")

    def commonToken(self, type_: int, text: str):
        stop = self.getCharIndex() - 1
        start = stop if text == "" else stop - len(text) + 1
        token = CommonToken(self._tokenFactorySourcePair, type_,
                            Lexer.DEFAULT_TOKEN_CHANNEL, start, stop)
        token.text = text
        return token

    @staticmethod
    def getIndentationCount(whitespace: str) -> int:
        count = 0
        for ch in whitespace:
            if ch == "\t":
                count += 8 - count % 8
            else:
                count += 1
        return count

    def atStartOfInput(self) -> bool:
        return self.getCharIndex() == 0

    def openBrace(self):
        self.opened += 1

    def closeBrace(self):
        self.opened -= 1

    def onNewLine(self):
        new_line = self.NEW_LINE_PATTERN.sub("", self.text)
        spaces = self.SPACES_PATTERN.sub("", self.text)

        next_ = self._input.LA(1)
        next_next = self._input.LA(2)
        # Dentro de (), [] o {} los saltos de línea no significan nada; y las
        # líneas vacías o de solo comentario tampoco (10='\n', 13='\r', 35='#').
        if self.opened > 0 or (next_next != -1 and next_ in (10, 13, 35)):
            self.skip()
            return

        self.emitToken(self.commonToken(self.NEWLINE, new_line))
        indent = self.getIndentationCount(spaces)
        previous = self.indents[-1] if self.indents else 0

        if indent == previous:
            self.skip()
        elif indent > previous:
            self.indents.append(indent)
            self.emitToken(self.commonToken(self.INDENT, spaces))
        else:
            while self.indents and self.indents[-1] > indent:
                self.emitToken(self.createDedent())
                self.indents.pop()
