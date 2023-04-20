# Generated from .\OrTex\OrTex.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OrTexParser import OrTexParser
else:
    from OrTexParser import OrTexParser

# This class defines a complete generic visitor for a parse tree produced by OrTexParser.

class OrTexVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OrTexParser#program.
    def visitProgram(self, ctx:OrTexParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#line.
    def visitLine(self, ctx:OrTexParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#statement.
    def visitStatement(self, ctx:OrTexParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#ifStatement.
    def visitIfStatement(self, ctx:OrTexParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#elseIfStatement.
    def visitElseIfStatement(self, ctx:OrTexParser.ElseIfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#whileStatement.
    def visitWhileStatement(self, ctx:OrTexParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#forStatement.
    def visitForStatement(self, ctx:OrTexParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#funDef.
    def visitFunDef(self, ctx:OrTexParser.FunDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#funDefReturn.
    def visitFunDefReturn(self, ctx:OrTexParser.FunDefReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#parameters.
    def visitParameters(self, ctx:OrTexParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#assignment.
    def visitAssignment(self, ctx:OrTexParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#varDefinition.
    def visitVarDefinition(self, ctx:OrTexParser.VarDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#functionCall.
    def visitFunctionCall(self, ctx:OrTexParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#objectFunctionCall.
    def visitObjectFunctionCall(self, ctx:OrTexParser.ObjectFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#objectFunctionCallFromFunction.
    def visitObjectFunctionCallFromFunction(self, ctx:OrTexParser.ObjectFunctionCallFromFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#objectCreationCall.
    def visitObjectCreationCall(self, ctx:OrTexParser.ObjectCreationCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classDef.
    def visitClassDef(self, ctx:OrTexParser.ClassDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classConstructor.
    def visitClassConstructor(self, ctx:OrTexParser.ClassConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classMethodDef.
    def visitClassMethodDef(self, ctx:OrTexParser.ClassMethodDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classQuestion.
    def visitClassQuestion(self, ctx:OrTexParser.ClassQuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classMethodCall.
    def visitClassMethodCall(self, ctx:OrTexParser.ClassMethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classMethodCallFromMethod.
    def visitClassMethodCallFromMethod(self, ctx:OrTexParser.ClassMethodCallFromMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#inplaceQuestion.
    def visitInplaceQuestion(self, ctx:OrTexParser.InplaceQuestionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classMethodCallExpression.
    def visitClassMethodCallExpression(self, ctx:OrTexParser.ClassMethodCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#constantExpression.
    def visitConstantExpression(self, ctx:OrTexParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#objectFunctionCallExpression.
    def visitObjectFunctionCallExpression(self, ctx:OrTexParser.ObjectFunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:OrTexParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:OrTexParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#notExpression.
    def visitNotExpression(self, ctx:OrTexParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:OrTexParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:OrTexParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#booleanExpression.
    def visitBooleanExpression(self, ctx:OrTexParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#functionExpression.
    def visitFunctionExpression(self, ctx:OrTexParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:OrTexParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#objectCreationCallExpression.
    def visitObjectCreationCallExpression(self, ctx:OrTexParser.ObjectCreationCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#classQuestionExpression.
    def visitClassQuestionExpression(self, ctx:OrTexParser.ClassQuestionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#multOp.
    def visitMultOp(self, ctx:OrTexParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#addOp.
    def visitAddOp(self, ctx:OrTexParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#compareOp.
    def visitCompareOp(self, ctx:OrTexParser.CompareOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#boolOp.
    def visitBoolOp(self, ctx:OrTexParser.BoolOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#constant.
    def visitConstant(self, ctx:OrTexParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#block.
    def visitBlock(self, ctx:OrTexParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OrTexParser#scope.
    def visitScope(self, ctx:OrTexParser.ScopeContext):
        return self.visitChildren(ctx)



del OrTexParser