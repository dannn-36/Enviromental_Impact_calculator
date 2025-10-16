from antlr4 import Parser

class CParserBase(Parser):
    def __init__(self, input):
        super().__init__(input)