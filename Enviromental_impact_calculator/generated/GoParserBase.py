"""Clase base del parser de Go (portada de antlr/grammars-v4).

La gramática de Go necesita algo de información semántica para desambiguar:
`pkg.Func` (identificador cualificado de un paquete importado) frente a
`Tipo.Metodo` (method expression). Para eso se guarda una tabla con los
nombres de los paquetes importados.
"""
import sys
from typing import TextIO

from antlr4 import Parser, Token, TokenStream


class GoParserBase(Parser):
    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.table = set()

    def myreset(self):
        self.table = set()

    def closingBracket(self) -> bool:
        la = self._input.LA(1)
        return la in (self.R_PAREN, self.R_CURLY, Token.EOF)

    def isNotReceive(self) -> bool:
        return self._input.LA(2) != self.RECEIVE

    def addImportSpec(self):
        ctx = self._ctx
        if not hasattr(ctx, "importPath"):
            return
        package_name = ctx.packageName() if hasattr(ctx, "packageName") else None
        if package_name is not None:
            self.table.add(package_name.getText())
            return
        path = ctx.importPath().getText().replace('"', "").replace("`", "")
        path = path.replace("\\", "/")
        last = path.split("/")[-1]
        self.table.add(last.split(".")[-1])

    def isOperand(self) -> bool:
        la = self._input.LT(1)
        if la.text == "err":
            return True
        if la.type != self.IDENTIFIER:
            return True
        # Un identificador que no va seguido de '.' siempre es un operando.
        if self._input.LT(2).type != self.DOT:
            return True
        # `x.(T)` es una aserción de tipo: x es un operando.
        if self._input.LT(3).type == self.L_PAREN:
            return True
        # `pkg.Nombre`: operando cualificado solo si pkg es un paquete importado.
        return la.text in self.table

    def isConversion(self) -> bool:
        return self._input.LT(1).type != self.IDENTIFIER

    def isMethodExpr(self) -> bool:
        la = self._input.LT(1)
        if la.type == self.STAR:
            return True
        if la.type != self.IDENTIFIER:
            return False
        return la.text not in self.table
