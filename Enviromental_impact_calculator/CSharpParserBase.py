from antlr4 import Parser

class CSharpParserBase(Parser):
    def __init__(self, input, output=None):
        super().__init__(input, output)