from antlr4 import Lexer

class GoLexerBase(Lexer):
    def __init__(self, input=None, output=None):
        super().__init__(input, output)