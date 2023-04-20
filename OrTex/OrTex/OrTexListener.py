# Generated from .\OrTex\OrTex.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OrTexParser import OrTexParser
else:
    from OrTexParser import OrTexParser

# This class defines a complete listener for a parse tree produced by OrTexParser.
class OrTexListener(ParseTreeListener):

    # Enter a parse tree produced by OrTexParser#program.
    def enterProgram(self, ctx:OrTexParser.ProgramContext):
        pass

    # Exit a parse tree produced by OrTexParser#program.
    def exitProgram(self, ctx:OrTexParser.ProgramContext):
        pass


    # Enter a parse tree produced by OrTexParser#line.
    def enterLine(self, ctx:OrTexParser.LineContext):
        pass

    # Exit a parse tree produced by OrTexParser#line.
    def exitLine(self, ctx:OrTexParser.LineContext):
        pass


    # Enter a parse tree produced by OrTexParser#statement.
    def enterStatement(self, ctx:OrTexParser.StatementContext):
        pass

    # Exit a parse tree produced by OrTexParser#statement.
    def exitStatement(self, ctx:OrTexParser.StatementContext):
        pass


    # Enter a parse tree produced by OrTexParser#ifStatement.
    def enterIfStatement(self, ctx:OrTexParser.IfStatementContext):
        pass

    # Exit a parse tree produced by OrTexParser#ifStatement.
    def exitIfStatement(self, ctx:OrTexParser.IfStatementContext):
        pass


    # Enter a parse tree produced by OrTexParser#elseIfStatement.
    def enterElseIfStatement(self, ctx:OrTexParser.ElseIfStatementContext):
        pass

    # Exit a parse tree produced by OrTexParser#elseIfStatement.
    def exitElseIfStatement(self, ctx:OrTexParser.ElseIfStatementContext):
        pass


    # Enter a parse tree produced by OrTexParser#whileStatement.
    def enterWhileStatement(self, ctx:OrTexParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by OrTexParser#whileStatement.
    def exitWhileStatement(self, ctx:OrTexParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by OrTexParser#forStatement.
    def enterForStatement(self, ctx:OrTexParser.ForStatementContext):
        pass

    # Exit a parse tree produced by OrTexParser#forStatement.
    def exitForStatement(self, ctx:OrTexParser.ForStatementContext):
        pass


    # Enter a parse tree produced by OrTexParser#funDef.
    def enterFunDef(self, ctx:OrTexParser.FunDefContext):
        pass

    # Exit a parse tree produced by OrTexParser#funDef.
    def exitFunDef(self, ctx:OrTexParser.FunDefContext):
        pass


    # Enter a parse tree produced by OrTexParser#funDefReturn.
    def enterFunDefReturn(self, ctx:OrTexParser.FunDefReturnContext):
        pass

    # Exit a parse tree produced by OrTexParser#funDefReturn.
    def exitFunDefReturn(self, ctx:OrTexParser.FunDefReturnContext):
        pass


    # Enter a parse tree produced by OrTexParser#parameters.
    def enterParameters(self, ctx:OrTexParser.ParametersContext):
        pass

    # Exit a parse tree produced by OrTexParser#parameters.
    def exitParameters(self, ctx:OrTexParser.ParametersContext):
        pass


    # Enter a parse tree produced by OrTexParser#assignment.
    def enterAssignment(self, ctx:OrTexParser.AssignmentContext):
        pass

    # Exit a parse tree produced by OrTexParser#assignment.
    def exitAssignment(self, ctx:OrTexParser.AssignmentContext):
        pass


    # Enter a parse tree produced by OrTexParser#varDefinition.
    def enterVarDefinition(self, ctx:OrTexParser.VarDefinitionContext):
        pass

    # Exit a parse tree produced by OrTexParser#varDefinition.
    def exitVarDefinition(self, ctx:OrTexParser.VarDefinitionContext):
        pass


    # Enter a parse tree produced by OrTexParser#functionCall.
    def enterFunctionCall(self, ctx:OrTexParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by OrTexParser#functionCall.
    def exitFunctionCall(self, ctx:OrTexParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by OrTexParser#objectFunctionCall.
    def enterObjectFunctionCall(self, ctx:OrTexParser.ObjectFunctionCallContext):
        pass

    # Exit a parse tree produced by OrTexParser#objectFunctionCall.
    def exitObjectFunctionCall(self, ctx:OrTexParser.ObjectFunctionCallContext):
        pass


    # Enter a parse tree produced by OrTexParser#objectFunctionCallFromFunction.
    def enterObjectFunctionCallFromFunction(self, ctx:OrTexParser.ObjectFunctionCallFromFunctionContext):
        pass

    # Exit a parse tree produced by OrTexParser#objectFunctionCallFromFunction.
    def exitObjectFunctionCallFromFunction(self, ctx:OrTexParser.ObjectFunctionCallFromFunctionContext):
        pass


    # Enter a parse tree produced by OrTexParser#objectCreationCall.
    def enterObjectCreationCall(self, ctx:OrTexParser.ObjectCreationCallContext):
        pass

    # Exit a parse tree produced by OrTexParser#objectCreationCall.
    def exitObjectCreationCall(self, ctx:OrTexParser.ObjectCreationCallContext):
        pass


    # Enter a parse tree produced by OrTexParser#classDef.
    def enterClassDef(self, ctx:OrTexParser.ClassDefContext):
        pass

    # Exit a parse tree produced by OrTexParser#classDef.
    def exitClassDef(self, ctx:OrTexParser.ClassDefContext):
        pass


    # Enter a parse tree produced by OrTexParser#classConstructor.
    def enterClassConstructor(self, ctx:OrTexParser.ClassConstructorContext):
        pass

    # Exit a parse tree produced by OrTexParser#classConstructor.
    def exitClassConstructor(self, ctx:OrTexParser.ClassConstructorContext):
        pass


    # Enter a parse tree produced by OrTexParser#classMethodDef.
    def enterClassMethodDef(self, ctx:OrTexParser.ClassMethodDefContext):
        pass

    # Exit a parse tree produced by OrTexParser#classMethodDef.
    def exitClassMethodDef(self, ctx:OrTexParser.ClassMethodDefContext):
        pass


    # Enter a parse tree produced by OrTexParser#classQuestion.
    def enterClassQuestion(self, ctx:OrTexParser.ClassQuestionContext):
        pass

    # Exit a parse tree produced by OrTexParser#classQuestion.
    def exitClassQuestion(self, ctx:OrTexParser.ClassQuestionContext):
        pass


    # Enter a parse tree produced by OrTexParser#classMethodCall.
    def enterClassMethodCall(self, ctx:OrTexParser.ClassMethodCallContext):
        pass

    # Exit a parse tree produced by OrTexParser#classMethodCall.
    def exitClassMethodCall(self, ctx:OrTexParser.ClassMethodCallContext):
        pass


    # Enter a parse tree produced by OrTexParser#classMethodCallFromMethod.
    def enterClassMethodCallFromMethod(self, ctx:OrTexParser.ClassMethodCallFromMethodContext):
        pass

    # Exit a parse tree produced by OrTexParser#classMethodCallFromMethod.
    def exitClassMethodCallFromMethod(self, ctx:OrTexParser.ClassMethodCallFromMethodContext):
        pass


    # Enter a parse tree produced by OrTexParser#inplaceQuestion.
    def enterInplaceQuestion(self, ctx:OrTexParser.InplaceQuestionContext):
        pass

    # Exit a parse tree produced by OrTexParser#inplaceQuestion.
    def exitInplaceQuestion(self, ctx:OrTexParser.InplaceQuestionContext):
        pass


    # Enter a parse tree produced by OrTexParser#classMethodCallExpression.
    def enterClassMethodCallExpression(self, ctx:OrTexParser.ClassMethodCallExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#classMethodCallExpression.
    def exitClassMethodCallExpression(self, ctx:OrTexParser.ClassMethodCallExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#constantExpression.
    def enterConstantExpression(self, ctx:OrTexParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#constantExpression.
    def exitConstantExpression(self, ctx:OrTexParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#objectFunctionCallExpression.
    def enterObjectFunctionCallExpression(self, ctx:OrTexParser.ObjectFunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#objectFunctionCallExpression.
    def exitObjectFunctionCallExpression(self, ctx:OrTexParser.ObjectFunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:OrTexParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:OrTexParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:OrTexParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:OrTexParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#notExpression.
    def enterNotExpression(self, ctx:OrTexParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#notExpression.
    def exitNotExpression(self, ctx:OrTexParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:OrTexParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:OrTexParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:OrTexParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:OrTexParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#booleanExpression.
    def enterBooleanExpression(self, ctx:OrTexParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#booleanExpression.
    def exitBooleanExpression(self, ctx:OrTexParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#functionExpression.
    def enterFunctionExpression(self, ctx:OrTexParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#functionExpression.
    def exitFunctionExpression(self, ctx:OrTexParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:OrTexParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:OrTexParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#objectCreationCallExpression.
    def enterObjectCreationCallExpression(self, ctx:OrTexParser.ObjectCreationCallExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#objectCreationCallExpression.
    def exitObjectCreationCallExpression(self, ctx:OrTexParser.ObjectCreationCallExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#classQuestionExpression.
    def enterClassQuestionExpression(self, ctx:OrTexParser.ClassQuestionExpressionContext):
        pass

    # Exit a parse tree produced by OrTexParser#classQuestionExpression.
    def exitClassQuestionExpression(self, ctx:OrTexParser.ClassQuestionExpressionContext):
        pass


    # Enter a parse tree produced by OrTexParser#multOp.
    def enterMultOp(self, ctx:OrTexParser.MultOpContext):
        pass

    # Exit a parse tree produced by OrTexParser#multOp.
    def exitMultOp(self, ctx:OrTexParser.MultOpContext):
        pass


    # Enter a parse tree produced by OrTexParser#addOp.
    def enterAddOp(self, ctx:OrTexParser.AddOpContext):
        pass

    # Exit a parse tree produced by OrTexParser#addOp.
    def exitAddOp(self, ctx:OrTexParser.AddOpContext):
        pass


    # Enter a parse tree produced by OrTexParser#compareOp.
    def enterCompareOp(self, ctx:OrTexParser.CompareOpContext):
        pass

    # Exit a parse tree produced by OrTexParser#compareOp.
    def exitCompareOp(self, ctx:OrTexParser.CompareOpContext):
        pass


    # Enter a parse tree produced by OrTexParser#boolOp.
    def enterBoolOp(self, ctx:OrTexParser.BoolOpContext):
        pass

    # Exit a parse tree produced by OrTexParser#boolOp.
    def exitBoolOp(self, ctx:OrTexParser.BoolOpContext):
        pass


    # Enter a parse tree produced by OrTexParser#constant.
    def enterConstant(self, ctx:OrTexParser.ConstantContext):
        pass

    # Exit a parse tree produced by OrTexParser#constant.
    def exitConstant(self, ctx:OrTexParser.ConstantContext):
        pass


    # Enter a parse tree produced by OrTexParser#block.
    def enterBlock(self, ctx:OrTexParser.BlockContext):
        pass

    # Exit a parse tree produced by OrTexParser#block.
    def exitBlock(self, ctx:OrTexParser.BlockContext):
        pass


    # Enter a parse tree produced by OrTexParser#scope.
    def enterScope(self, ctx:OrTexParser.ScopeContext):
        pass

    # Exit a parse tree produced by OrTexParser#scope.
    def exitScope(self, ctx:OrTexParser.ScopeContext):
        pass



del OrTexParser