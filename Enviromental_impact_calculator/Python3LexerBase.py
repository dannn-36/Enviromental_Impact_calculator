from antlr4 import Lexer

class Python3LexerBase(Lexer):
    def __init__(self, input=None, output=None):
        super().__init__(input, output)
        self.nesting = 0

    def atStartOfInput(self):
        return self._input.index == 0

    def openBrace(self):
        self.nesting += 1

    def closeBrace(self):
        self.nesting -= 1

    def onNewLine(self):
        pass