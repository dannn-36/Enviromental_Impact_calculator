from antlr4 import Lexer

class Python3LexerBase(Lexer):
    def __init__(self, input):
        super().__init__(input)
        self.nesting = 0

    def emitToken(self, token):
        return super().emitToken(token)

    def nextToken(self):
        return super().nextToken()

    def atStartOfInput(self):
        return self._input.index == 0

    def openBrace(self):
        self.nesting += 1

    def closeBrace(self):
        self.nesting -= 1

    def onNewLine(self):
        pass