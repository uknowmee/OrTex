import copy
import sys

import OrTex.Class
from OrTex.Functions import SysFunction, UserFunction, UserMethod
from OrTex.Class import List, Dict, Scope, Class, Object, Function
from OrTex.ErrorHandler import ErrorHandler
from OrTex.Visualisation import Space
from OrTex.OrTex.OrTexVisitor import OrTexVisitor
from OrTex.OrTex.OrTexParser import OrTexParser


class MyVisitor(OrTexVisitor):
    lastLine = int()

    variables = dict()
    functions = dict()
    classes = dict()

    runningFunctions = []
    objectsWithMethodRunning = []
    scopes = []

    scanningFunction = False
    scanningClass = False
    scanningClassConstructor = False
    scanningClassMethod = False

    startPoint = None

    objectTypes_ = [(Dict, Dict("Dict")),
                    (List, List("List")),
                    (Space, Space(0, 0, "Space"))]

    def __errorAtLine__(self):
        print("Error at line: ", self.lastLine)

    def __scopeAdd__(self):
        # Adds existing scope to scope stack <-it just helps to count and debug.
        sc = Scope(len(self.scopes))
        self.scopes.append(sc)

        # Adds scope variable to classic function or Main function stack.
        if len(self.runningFunctions) > 0:
            self.runningFunctions[len(self.runningFunctions) - 1].variables[sc.name] = sc
        else:
            self.variables[sc.name] = sc

        return sc.name

    def __scopeRemove__(self, scope_name):
        # Gets list<variable names> of current stack (function or Main).
        if len(self.runningFunctions) > 0:
            keys = list(self.runningFunctions[len(self.runningFunctions) - 1].variables.keys())
        else:
            keys = list(self.variables.keys())

        # Reverse order of variables fetched from stack.
        # Removes variables from (function or Main) stack as long as scope "flag" variable isn't removed.
        keys.reverse()
        for it in keys:
            if len(self.runningFunctions) > 0:
                self.runningFunctions[len(self.runningFunctions) - 1].variables.pop(it)
            else:
                self.variables.pop(it)

            if it == scope_name:
                break

        # Remove finished scope from scope stack
        self.scopes.pop(len(self.scopes) - 1)

    @staticmethod
    def __keywordOrExisting__(self, used_str):
        for functionName in SysFunction.FNames:
            if used_str == functionName.name:
                ErrorHandler.stringIsNotAvailable(self, used_str)

        if used_str in ["IDENTIFIER", "COMMENT", "NULL", "BOOL", "STRING", "DOUBLE", "INTEGER"]:
            ErrorHandler.stringIsNotAvailable(self, used_str)

        if used_str in ["and", "or", "xor", "@", "true", "false", "null"]:
            ErrorHandler.stringIsNotAvailable(self, used_str)

        if used_str in ["for", "func", "and", "while", "if", "else"]:
            ErrorHandler.stringIsNotAvailable(self, used_str)

    @staticmethod
    def __increment__(self, value, increment, operation):
        if operation == '+':
            value += increment
        elif operation == '-':
            value -= increment
        elif operation == '*':
            value *= increment
        else:
            ErrorHandler.noSuchIncrement(self)
        return value

    @staticmethod
    def __fromOFCall__(self, var, to_return, next_f_calls, object_types):
        try:
            for obj in object_types:
                if to_return.type == obj[1].type:
                    to_return.methodCall(next_f_calls[0][0], next_f_calls[0][1])
                    var.toReturn = to_return.toReturn
                    break
        except:
            if type(to_return) == OrTex.Class.Object or type(to_return) == Object:
                method = to_return.methods[next_f_calls[0][0]]

                j = 0
                for v in method[1].keys():
                    method[1][v] = next_f_calls[0][1][j]
                    j += 1

                self.objectsWithMethodRunning.append(to_return)
                self.runningFunctions.append(
                    Function(next_f_calls[0], len(self.runningFunctions), copy.deepcopy(method[1]), {}, method[2]))

                self.visit(method[0])
                to_return = self.objectsWithMethodRunning.pop(len(self.objectsWithMethodRunning) - 1)
                try:
                    to_return.toReturn = self.runningFunctions[len(self.runningFunctions) - 1].variables[method[2]]
                except:
                    to_return.toReturn = None

                var.toReturn = to_return.toReturn

                to_return.toReturn = None
                self.runningFunctions.pop(len(self.runningFunctions) - 1)
            else:
                ErrorHandler.functionUsedOnBaseTypeObject(self, type(to_return))
        return var

    def visitAssignment(self, ctx):
        if ctx.classQuestion():
            objName, fieldName = self.visit(ctx.classQuestion())
            if objName == "this":
                if len(self.runningFunctions) > 0:
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[fieldName] = None
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[
                        fieldName] = self.visit(ctx.expression())
                else:
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[fieldName] = None
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[
                        fieldName] = self.visit(ctx.expression())
                return "this"
            else:
                if len(self.runningFunctions) > 0:
                    if objName not in self.runningFunctions[len(self.runningFunctions) - 1].variables.keys():
                        pass
                    self.runningFunctions[len(self.runningFunctions) - 1].variables[objName].fields[
                        fieldName] = self.visit(ctx.expression())
                else:
                    if objName not in self.variables.keys():
                        pass
                    self.variables[objName].fields[fieldName] = self.visit(ctx.expression())
                return objName

        name = str(ctx.IDENTIFIER())

        self.__keywordOrExisting__(self, name)

        if len(self.runningFunctions) > 0:
            if name not in self.runningFunctions[len(self.runningFunctions) - 1].variables.keys():
                self.runningFunctions[len(self.runningFunctions) - 1].variables[name] = None
            self.runningFunctions[len(self.runningFunctions) - 1].variables[name] = self.visit(ctx.expression())
        else:
            if name not in self.variables.keys():
                self.variables[name] = None
            self.variables[name] = self.visit(ctx.expression())

        return name

    def visitVarDefinition(self, ctx: OrTexParser.VarDefinitionContext):
        if ctx.classQuestion():
            objName, fieldName = self.visit(ctx.classQuestion())
            if objName == "this":
                if len(self.runningFunctions) > 0:
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[fieldName] = None
                else:
                    self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[fieldName] = None
                return "this"

        name = str(ctx.IDENTIFIER())

        self.__keywordOrExisting__(self, name)

        if len(self.runningFunctions) > 0:
            self.runningFunctions[len(self.runningFunctions) - 1].variables[name] = None
        else:
            self.variables[name] = None

        return name

    def visitConstant(self, ctx: OrTexParser.ConstantContext):
        if ctx.INTEGER() is not None:
            return int(ctx.getText())
        if ctx.DOUBLE() is not None:
            return float(ctx.getText())
        if ctx.STRING() is not None:
            ret = str(ctx.getText())
            for char in ['\'', '"']:
                ret = ret.replace(char, "")
            for char in ["\\n"]:
                ret = ret.replace(char, '\n')
            for char in ["\\t"]:
                ret = ret.replace(char, '\t')
            return ret
        if ctx.BOOL() is not None:
            return ctx.getText() == 'true'
        if ctx.NULL() is not None:
            return None
        else:
            ErrorHandler.noSuchConstant(self)

    def visitIdentifierExpression(self, ctx: OrTexParser.IdentifierExpressionContext):
        name = str(ctx.IDENTIFIER())
        self.__keywordOrExisting__(self, name)

        if len(self.runningFunctions) > 0:
            if name not in self.runningFunctions[len(self.runningFunctions) - 1].variables:
                ErrorHandler.variableDontExistInFunctionScope(self, name)
            return self.runningFunctions[len(self.runningFunctions) - 1].variables[name]
        else:
            if name not in self.variables:
                ErrorHandler.variableDontExistInScope(self, name)
            return self.variables[name]

    def visitAdditiveExpression(self, ctx: OrTexParser.AdditiveExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        op = ctx.addOp().getText()
        if type(left) == bool or type(right) == bool:
            ErrorHandler.AddingBool(self)

        if left is None or right is None:
            ErrorHandler.AddingNone(self)

        if (type(left) == int or type(left) == float) and type(right) == str:
            operation = {
                '+': lambda: str(left) + right,
            }
        elif (type(right) == int or type(right) == float) and type(left) == str:
            operation = {
                '+': lambda: left + str(right),
            }
        else:
            operation = {
                '+': lambda: left + right,
                '-': lambda: left - right,
            }

        return operation.get(op, lambda: None)()

    def visitMultiplicativeExpression(self, ctx: OrTexParser.MultiplicativeExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if type(right) == bool or type(left) == bool:
            ErrorHandler.MultiplicationBool(self)

        if (type(left) == float and type(right) == str) or (type(right) == float and type(left) == str):
            ErrorHandler.MultiplicationTypeFault(self)

        if left is None or right is None:
            ErrorHandler.MultiplicationNone(self)

        op = ctx.multOp().getText()

        if op == '/' and (type(left) == str or type(right) == str):
            ErrorHandler.MultiplicationTypeFault(self)

        if op == '/' and (right == 0):
            ErrorHandler.DivisionBy0(self)

        operation = {
            '*': lambda: left * right,
            '/': lambda: left / right,
        }
        return operation.get(op, lambda: None)()

    def visitComparisonExpression(self, ctx: OrTexParser.ComparisonExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if (type(left) != type(right)) and (left is not None and right is not None):
            ErrorHandler.ComparisonTypesFault(self)

        op = ctx.compareOp().getText()
        operation = {
            '==': lambda: left == right,
            '!=': lambda: left != right,
            '>': lambda: left > right,
            '<': lambda: left < right,
            '>=': lambda: left >= right,
            '<=': lambda: left <= right,
        }
        return operation.get(op, lambda: None)()

    def visitConstantExpression(self, ctx: OrTexParser.ConstantExpressionContext):
        sth = self.visit(ctx.constant())
        return sth

    def visitParenthesizedExpression(self, ctx: OrTexParser.ParenthesizedExpressionContext):
        sth = self.visit(ctx.expression())
        return sth

    def visitNotExpression(self, ctx: OrTexParser.NotExpressionContext):
        sth = self.visit(ctx.expression())
        if sth:
            return False
        else:
            return True

    def visitWhileStatement(self, ctx: OrTexParser.WhileStatementContext):
        scopeName = self.__scopeAdd__()

        while self.visit(ctx.expression()):
            self.visit(ctx.block())

        self.__scopeRemove__(scopeName)

    def visitForStatement(self, ctx: OrTexParser.ForStatementContext):
        scopeName = self.__scopeAdd__()

        iterName = self.visit(ctx.assignment())
        operation = ctx.children[6].symbol.text

        while self.visit(ctx.expression()):
            self.visit(ctx.block())

            try:
                incrName = ctx.IDENTIFIER().symbol.text
                if len(self.runningFunctions) > 0:
                    increment = self.runningFunctions[len(self.runningFunctions) - 1].variables[incrName]
                    value = self.runningFunctions[len(self.runningFunctions) - 1].variables[iterName]
                else:
                    increment = self.variables[incrName]
                    value = self.variables[iterName]
            except:
                increment = int(ctx.children[7].symbol.text)
                if len(self.runningFunctions) > 0:
                    value = self.runningFunctions[len(self.runningFunctions) - 1].variables[iterName]
                else:
                    value = self.variables[iterName]

            value = self.__increment__(self, value, increment, operation)

            if len(self.runningFunctions) > 0:
                self.runningFunctions[len(self.runningFunctions) - 1].variables[iterName] = value
            else:
                self.variables[iterName] = value

        self.__scopeRemove__(scopeName)

    def visitFunDef(self, ctx: OrTexParser.FunDefContext):
        self.scanningFunction = True
        name = str(ctx.IDENTIFIER())
        self.__keywordOrExisting__(self, name)

        if name in self.functions.keys():
            ErrorHandler.FunctionExists(self, name)

        if name == "MAIN" and self.startPoint is None:
            self.startPoint = ctx.block()
        elif name == "MAIN" and self.startPoint is not None:
            ErrorHandler.FunctionMainFault(self)

        try:
            ret = str(ctx.funDefReturn().IDENTIFIER())
        except:
            ret = None
        self.functions[name] = [ctx.block(), dict(), ret]

        for param in self.visit(ctx.parameters()):
            self.functions[name][1][str(param.IDENTIFIER())] = None

        self.scanningFunction = False

    def visitFunctionExpression(self, ctx: OrTexParser.FunctionExpressionContext):
        ret = self.visit(ctx.functionCall())
        if ctx.inplaceQuestion():
            ret = ret.fields[str(ctx.children[1].IDENTIFIER())]
        return ret

    def visitFunctionCall(self, ctx: OrTexParser.FunctionCallContext):
        if self.scanningFunction:
            return

        name = str(ctx.IDENTIFIER())
        for fName in SysFunction.FNames:
            if name == fName.name:
                doSomething = getattr(SysFunction, str(ctx.IDENTIFIER()))
                doSomething(self, ctx)
                return

        if str(ctx.IDENTIFIER()) in self.functions.keys():
            ret = UserFunction.userDefinedFunction(self, ctx)
            UserFunction.referenceReturnFromUserDefinedFunction(self)
            self.runningFunctions.pop(len(self.runningFunctions) - 1)
            return ret

        if str(ctx.IDENTIFIER()) not in self.functions.keys():
            ErrorHandler.FunctionNotExists(self, ctx.IDENTIFIER())

    def visitObjectFunctionCallFromFunction(self, ctx: OrTexParser.ObjectFunctionCallFromFunctionContext):
        if type(ctx.children) == list:
            ret = []
            name = 1
            param = 3
            args = []
            while param < len(ctx.children):

                smth = self.visit(ctx.children[param])
                args.clear()
                if len(self.runningFunctions) > 0:
                    for it in smth:
                        varDict = self.runningFunctions[len(self.runningFunctions) - 1].variables
                        try:
                            args.append(varDict[str(it.IDENTIFIER())])
                        except:
                            args.append(self.visit(it))
                else:
                    for it in smth:
                        try:
                            args.append(self.variables[str(it.IDENTIFIER())])
                        except:
                            args.append(self.visit(it))

                ret.append((ctx.children[name].symbol.text, copy.deepcopy(args)))
                name += 5
                param += 5
            return ret

        return list()

    def visitObjectFunctionCallExpression(self, ctx:OrTexParser.ObjectFunctionCallExpressionContext):
        ret = self.visit(ctx.objectFunctionCall())
        if ctx.inplaceQuestion():
            ret = ret.fields[str(ctx.children[1].IDENTIFIER())]
        return ret

    def visitObjectFunctionCall(self, ctx: OrTexParser.ObjectFunctionCallContext):
        if self.scanningFunction:
            return

        try:
            if len(self.runningFunctions) > 0:
                if type(self.runningFunctions[len(self.runningFunctions) - 1].variables[
                            ctx.children[0].getText()]) == Object:
                    return self.visitClassMethodCall(ctx)
            else:
                if type(self.variables[ctx.children[0].getText()]) == Object:
                    return self.visitClassMethodCall(ctx)
        except:
            pass

        varName = ctx.children[0].getText()
        functionName = ctx.children[2].getText()
        args = SysFunction.__scan_args__(self, ctx)
        toReturn = None

        if len(self.runningFunctions) > 0:
            var = self.runningFunctions[len(self.runningFunctions) - 1].variables[varName]
        else:
            var = self.variables[varName]

        objectTypes = self.objectTypes_

        for obj in objectTypes:
            if var.type == obj[1].type:
                var = var.methodCall(functionName, args)
                toReturn = var.toReturn

                next_f_calls = self.visit(ctx.objectFunctionCallFromFunction())
                while len(next_f_calls) > 0:
                    var = self.__fromOFCall__(self, var, toReturn, next_f_calls, objectTypes)
                    toReturn = var.toReturn
                    next_f_calls.pop(0)

                var.toReturn = None
                break

        if len(self.runningFunctions) > 0:
            self.runningFunctions[len(self.runningFunctions) - 1].variables[varName] = var
        else:
            self.variables[varName] = var

        return toReturn

    def visitObjectCreationCall(self, ctx: OrTexParser.ObjectCreationCallContext):
        if self.scanningFunction:
            return

        name = str(ctx.IDENTIFIER())

        for ofName in SysFunction.OFNames:
            if name == ofName.name:
                doSomething = getattr(SysFunction, str(ctx.IDENTIFIER()))
                return doSomething(self, ctx)

        for classname in self.classes.keys():
            if name == classname:
                obj = Object(classname, copy.deepcopy(self.classes[classname].fields), self.classes[classname].methods)
                self.objectsWithMethodRunning.append(obj)
                UserMethod.userConstructor(self, ctx)
                self.runningFunctions.pop(len(self.runningFunctions) - 1)
                self.objectsWithMethodRunning.pop(len(self.objectsWithMethodRunning) - 1)
                return obj

    def visitParameters(self, ctx: OrTexParser.ParametersContext):
        ids = []
        for ident in ctx.expression():
            ids.append(ident)
        return ids

    def visitIfStatement(self, ctx: OrTexParser.IfStatementContext):
        sth = self.visit(ctx.expression())

        if sth:
            scopeName = self.__scopeAdd__()
            self.visit(ctx.block())
            self.__scopeRemove__(scopeName)
        else:
            try:
                scopeName = self.__scopeAdd__()
                self.visit(ctx.elseIfStatement())
                self.__scopeRemove__(scopeName)
            except:
                pass

    def visitBooleanExpression(self, ctx: OrTexParser.BooleanExpressionContext):
        exp = []

        ids = []
        for ident in ctx.expression():
            ids.append(ident)

        comp = ctx.boolOp().getText()

        if comp not in ['and', 'or']:
            ErrorHandler.WrongBoolOperator(self)

        for ex in ids:
            exp.append(self.visit(ex))

        if comp == "and":
            if exp[0] and exp[1]:
                return True
        if comp == "or":
            if exp[0] or exp[1]:
                return True

        return False

    def visitLine(self, ctx: OrTexParser.LineContext):
        self.lastLine = ctx.stop.line

        if self.scanningClassConstructor:
            if type(ctx.children[0]) == OrTexParser.StatementContext:
                if type(ctx.children[0].children[0]) == OrTexParser.VarDefinitionContext:
                    if type(ctx.children[0].children[0].children[0]) == OrTexParser.ClassQuestionContext:
                        return str(ctx.children[0].children[0].children[0].children[2])
                elif type(ctx.children[0].children[0]) == OrTexParser.AssignmentContext:
                    if type(ctx.children[0].children[0].children[0]) == OrTexParser.ClassQuestionContext:
                        return str(ctx.children[0].children[0].children[0].children[2])

                return ""

        return self.visitChildren(ctx)

    def visitScope(self, ctx: OrTexParser.ScopeContext):
        scopeName = self.__scopeAdd__()

        # Execute code inside the scope.
        self.visitChildren(ctx)

        self.__scopeRemove__(scopeName)

    def visitClassDef(self, ctx: OrTexParser.ClassDefContext):
        self.scanningClass = True
        self.scanningClassConstructor = True
        self.scanningClassMethod = True

        className = str(ctx.IDENTIFIER())
        (classFields, classConstructor) = self.visit(ctx.classConstructor())
        classMethods = dict()

        for method in ctx.classMethodDef():
            tempMethod = self.visit(method)
            if tempMethod[0] not in classMethods.keys():
                classMethods[tempMethod[0]] = [tempMethod[1], tempMethod[2], tempMethod[3]]
            else:
                sys.exit(-1000)

        if className not in self.classes.keys():
            self.classes[className] = Class(className, len(self.classes.keys()) - 1, classFields, classMethods,
                                            classConstructor)
        else:
            sys.exit(-1000)

        self.scanningClass = False
        self.scanningClassConstructor = False
        self.scanningClassMethod = False

    def visitClassConstructor(self, ctx: OrTexParser.ClassConstructorContext):
        block = ctx.block()
        variables = dict()
        parameters = dict()

        for sth in block.children:
            if type(sth) == OrTexParser.LineContext:
                probVar = self.visit(sth)
                if probVar != "" and (probVar not in variables.keys()):
                    variables[probVar] = None

        for param in self.visit(ctx.parameters()):
            parameters[str(param.IDENTIFIER())] = None

        return variables, [block, parameters]

    def visitClassMethodDef(self, ctx: OrTexParser.ClassMethodDefContext):
        name = str(ctx.IDENTIFIER())
        self.__keywordOrExisting__(self, name)

        try:
            ret = str(ctx.funDefReturn().IDENTIFIER())
        except:
            ret = None
        function = [name, ctx.block(), dict(), ret]

        for param in self.visit(ctx.parameters()):
            function[2][str(param.IDENTIFIER())] = None

        return function

    def visitClassQuestionExpression(self, ctx: OrTexParser.ClassQuestionExpressionContext):
        objName, varName = str(ctx.children[0].children[0]), str(ctx.children[0].children[2])

        if len(self.runningFunctions) > 0:
            if objName not in self.runningFunctions[len(self.runningFunctions) - 1].variables.keys():
                return self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[varName]
            return self.runningFunctions[len(self.runningFunctions) - 1].variables[objName].fields[varName]
        else:
            if objName not in self.variables.keys():
                return self.objectsWithMethodRunning[len(self.objectsWithMethodRunning) - 1].fields[varName]
            return self.variables[objName].fields[varName]

    def visitClassQuestion(self, ctx: OrTexParser.ClassQuestionContext):
        if str(ctx.children[0]) == "this":
            return str(ctx.children[0]), str(ctx.children[2])

        return str(ctx.children[0]), str(ctx.children[2])

    def visitClassMethodCall(self, ctx: OrTexParser.ClassMethodCallContext):
        objName = str(ctx.children[0])
        methodName = str(ctx.children[2])
        obj = None

        if objName == "this":
            obj = self.objectsWithMethodRunning[len(self.objectsWithMethodRunning)]

            ret = UserMethod.userDefinedMethod(self, obj.methods[methodName], ctx)
            UserMethod.referenceReturnFromUserDefinedMethod(self)

            self.runningFunctions.pop(len(self.runningFunctions) - 1)
            return ret

        if len(self.runningFunctions) > 0:
            obj = self.runningFunctions[len(self.runningFunctions) - 1].variables[objName]
        else:
            obj = self.variables[objName]

        if methodName in obj.methods.keys():
            self.objectsWithMethodRunning.append(obj)

            ret = UserMethod.userDefinedMethod(self, obj.methods[methodName], ctx)
            UserMethod.referenceReturnFromUserDefinedMethod(self)

            self.runningFunctions.pop(len(self.runningFunctions) - 1)
            self.objectsWithMethodRunning.pop(len(self.objectsWithMethodRunning) - 1)
            return ret

    def visitClassMethodCallFromMethod(self, ctx: OrTexParser.ClassMethodCallFromMethodContext):
        pass
