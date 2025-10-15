from antlr4 import Parser

class Python3ParserBase(Parser):
    def __init__(self, input):
        super().__init__(input)