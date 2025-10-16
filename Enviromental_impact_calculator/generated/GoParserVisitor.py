# Generated from grammars/GoParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GoParser import GoParser
else:
    from GoParser import GoParser

# This class defines a complete generic visitor for a parse tree produced by GoParser.

class GoParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GoParser#sourceFile.
    def visitSourceFile(self, ctx:GoParser.SourceFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#packageClause.
    def visitPackageClause(self, ctx:GoParser.PackageClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#packageName.
    def visitPackageName(self, ctx:GoParser.PackageNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#identifier.
    def visitIdentifier(self, ctx:GoParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#importDecl.
    def visitImportDecl(self, ctx:GoParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#importSpec.
    def visitImportSpec(self, ctx:GoParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#importPath.
    def visitImportPath(self, ctx:GoParser.ImportPathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#declaration.
    def visitDeclaration(self, ctx:GoParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#constDecl.
    def visitConstDecl(self, ctx:GoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#constSpec.
    def visitConstSpec(self, ctx:GoParser.ConstSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#identifierList.
    def visitIdentifierList(self, ctx:GoParser.IdentifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#expressionList.
    def visitExpressionList(self, ctx:GoParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeDecl.
    def visitTypeDecl(self, ctx:GoParser.TypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeSpec.
    def visitTypeSpec(self, ctx:GoParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#aliasDecl.
    def visitAliasDecl(self, ctx:GoParser.AliasDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeDef.
    def visitTypeDef(self, ctx:GoParser.TypeDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeParameters.
    def visitTypeParameters(self, ctx:GoParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeParameterDecl.
    def visitTypeParameterDecl(self, ctx:GoParser.TypeParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeElement.
    def visitTypeElement(self, ctx:GoParser.TypeElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeTerm.
    def visitTypeTerm(self, ctx:GoParser.TypeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#functionDecl.
    def visitFunctionDecl(self, ctx:GoParser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#methodDecl.
    def visitMethodDecl(self, ctx:GoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#receiver.
    def visitReceiver(self, ctx:GoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#varDecl.
    def visitVarDecl(self, ctx:GoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#varSpec.
    def visitVarSpec(self, ctx:GoParser.VarSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#block.
    def visitBlock(self, ctx:GoParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#statementList.
    def visitStatementList(self, ctx:GoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#statement.
    def visitStatement(self, ctx:GoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#simpleStmt.
    def visitSimpleStmt(self, ctx:GoParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#expressionStmt.
    def visitExpressionStmt(self, ctx:GoParser.ExpressionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#sendStmt.
    def visitSendStmt(self, ctx:GoParser.SendStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#incDecStmt.
    def visitIncDecStmt(self, ctx:GoParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#assignment.
    def visitAssignment(self, ctx:GoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#assign_op.
    def visitAssign_op(self, ctx:GoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#shortVarDecl.
    def visitShortVarDecl(self, ctx:GoParser.ShortVarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#labeledStmt.
    def visitLabeledStmt(self, ctx:GoParser.LabeledStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#returnStmt.
    def visitReturnStmt(self, ctx:GoParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#breakStmt.
    def visitBreakStmt(self, ctx:GoParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#continueStmt.
    def visitContinueStmt(self, ctx:GoParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#gotoStmt.
    def visitGotoStmt(self, ctx:GoParser.GotoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#fallthroughStmt.
    def visitFallthroughStmt(self, ctx:GoParser.FallthroughStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#deferStmt.
    def visitDeferStmt(self, ctx:GoParser.DeferStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#ifStmt.
    def visitIfStmt(self, ctx:GoParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#switchStmt.
    def visitSwitchStmt(self, ctx:GoParser.SwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#exprSwitchStmt.
    def visitExprSwitchStmt(self, ctx:GoParser.ExprSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#exprCaseClause.
    def visitExprCaseClause(self, ctx:GoParser.ExprCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#exprSwitchCase.
    def visitExprSwitchCase(self, ctx:GoParser.ExprSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeSwitchStmt.
    def visitTypeSwitchStmt(self, ctx:GoParser.TypeSwitchStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeSwitchGuard.
    def visitTypeSwitchGuard(self, ctx:GoParser.TypeSwitchGuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeCaseClause.
    def visitTypeCaseClause(self, ctx:GoParser.TypeCaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeSwitchCase.
    def visitTypeSwitchCase(self, ctx:GoParser.TypeSwitchCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeList.
    def visitTypeList(self, ctx:GoParser.TypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#selectStmt.
    def visitSelectStmt(self, ctx:GoParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#commClause.
    def visitCommClause(self, ctx:GoParser.CommClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#commCase.
    def visitCommCase(self, ctx:GoParser.CommCaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#recvStmt.
    def visitRecvStmt(self, ctx:GoParser.RecvStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#forStmt.
    def visitForStmt(self, ctx:GoParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#condition.
    def visitCondition(self, ctx:GoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#forClause.
    def visitForClause(self, ctx:GoParser.ForClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#rangeClause.
    def visitRangeClause(self, ctx:GoParser.RangeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#goStmt.
    def visitGoStmt(self, ctx:GoParser.GoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#type_.
    def visitType_(self, ctx:GoParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeArgs.
    def visitTypeArgs(self, ctx:GoParser.TypeArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeName.
    def visitTypeName(self, ctx:GoParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeLit.
    def visitTypeLit(self, ctx:GoParser.TypeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#arrayType.
    def visitArrayType(self, ctx:GoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#arrayLength.
    def visitArrayLength(self, ctx:GoParser.ArrayLengthContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#elementType.
    def visitElementType(self, ctx:GoParser.ElementTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#pointerType.
    def visitPointerType(self, ctx:GoParser.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#interfaceType.
    def visitInterfaceType(self, ctx:GoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#sliceType.
    def visitSliceType(self, ctx:GoParser.SliceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#mapType.
    def visitMapType(self, ctx:GoParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#channelType.
    def visitChannelType(self, ctx:GoParser.ChannelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#methodSpec.
    def visitMethodSpec(self, ctx:GoParser.MethodSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#functionType.
    def visitFunctionType(self, ctx:GoParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#signature.
    def visitSignature(self, ctx:GoParser.SignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#result.
    def visitResult(self, ctx:GoParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#parameters.
    def visitParameters(self, ctx:GoParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#parameterDecl.
    def visitParameterDecl(self, ctx:GoParser.ParameterDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#expression.
    def visitExpression(self, ctx:GoParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:GoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#conversion.
    def visitConversion(self, ctx:GoParser.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#operand.
    def visitOperand(self, ctx:GoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#literal.
    def visitLiteral(self, ctx:GoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#basicLit.
    def visitBasicLit(self, ctx:GoParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#integer.
    def visitInteger(self, ctx:GoParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#operandName.
    def visitOperandName(self, ctx:GoParser.OperandNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#qualifiedIdent.
    def visitQualifiedIdent(self, ctx:GoParser.QualifiedIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#compositeLit.
    def visitCompositeLit(self, ctx:GoParser.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#literalType.
    def visitLiteralType(self, ctx:GoParser.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#literalValue.
    def visitLiteralValue(self, ctx:GoParser.LiteralValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#elementList.
    def visitElementList(self, ctx:GoParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#keyedElement.
    def visitKeyedElement(self, ctx:GoParser.KeyedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#key.
    def visitKey(self, ctx:GoParser.KeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#element.
    def visitElement(self, ctx:GoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#structType.
    def visitStructType(self, ctx:GoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#fieldDecl.
    def visitFieldDecl(self, ctx:GoParser.FieldDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#string_.
    def visitString_(self, ctx:GoParser.String_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#embeddedField.
    def visitEmbeddedField(self, ctx:GoParser.EmbeddedFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#functionLit.
    def visitFunctionLit(self, ctx:GoParser.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#index.
    def visitIndex(self, ctx:GoParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#slice_.
    def visitSlice_(self, ctx:GoParser.Slice_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#typeAssertion.
    def visitTypeAssertion(self, ctx:GoParser.TypeAssertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#arguments.
    def visitArguments(self, ctx:GoParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#methodExpr.
    def visitMethodExpr(self, ctx:GoParser.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GoParser#eos.
    def visitEos(self, ctx:GoParser.EosContext):
        return self.visitChildren(ctx)



del GoParser