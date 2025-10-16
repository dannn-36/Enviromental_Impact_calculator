from antlr4 import Parser

class GoParserBase(Parser):
    def __init__(self, input):
        super().__init__(input)