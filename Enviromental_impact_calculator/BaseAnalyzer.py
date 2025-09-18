import numpy as np
import antlr4 as antlr
import sys as sys
import os as os
import pandas as pd
class BaseAnalyzer:
    
    def __init__(self):
        pass
    
    def parse(self, input_stream, lexer_class, parser_class, visitor_class):
        lexer = lexer_class(input_stream)
        stream = antlr.CommonTokenStream(lexer)
        parser = parser_class(stream)
        tree = parser.prog()
        visitor = visitor_class()
        return visitor.visit(tree)
    
    def get_visitor(self, visitor_class):
        return visitor_class()
    def analyze(self, input_data, lexer_class, parser_class, visitor_class):
        input_stream = antlr.InputStream(input_data)
        return self.parse(input_stream, lexer_class, parser_class, visitor_class)