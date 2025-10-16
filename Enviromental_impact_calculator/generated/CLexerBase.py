from antlr4 import Lexer

class CLexerBase(Lexer):
    def __init__(self, input=None, output=None):
        super().__init__(input, output)