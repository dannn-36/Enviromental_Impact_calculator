from antlr4 import Lexer

class Python3LexerBase(Lexer):
    def __init__(self, input=None, output=None):
        super().__init__(input, output)