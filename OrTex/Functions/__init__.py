from copy import deepcopy
import enum
from OrTex.OrTex.OrTexParser import OrTexParser
import OrTex.Class as Cl
from OrTex.Visualisation import Space as Sp
import sys


class SysFunction:
    class FNames(enum.Enum):
        write = 1

    class OFNames(enum.Enum):
        List = 1
        Dict = 2
        Space = 3

    @staticmethod
    def __scan_args__(self, ctx: OrTexParser.FunctionCallContext):
        smth = self.visit(ctx.parameters())
        ret = []

        if len(self.runningFunctions) > 0:
            for it in smth:
                varDict = self.runningFunctions[len(self.runningFunctions) - 1].variables
                try:
                    ret.append(varDict[str(it.IDENTIFIER())])
                except:
                    ret.append(self.visit(it))
        else:
            for it in smth:
                try:
                    ret.append(self.variables[str(it.IDENTIFIER())])
                except:
                    ret.append(self.visit(it))
        return ret

    @staticmethod
    def __scan_args_object_creation__(self, ctx: OrTexParser.ObjectCreationCallContext):
        smth = self.visit(ctx.parameters())
        try:
            ret = [str(ctx.parentCtx.parentCtx.IDENTIFIER())]
        except:
            ret = []

        if len(self.runningFunctions) > 0:
            for it in smth:
                varDict = self.runningFunctions[len(self.runningFunctions) - 1].variables
                try:
                    ret.append(varDict[str(it.IDENTIFIER())])
                except:
                    ret.append(self.visit(it))
        else:
            for it in smth:
                try:
                    ret.append(self.variables[str(it.IDENTIFIER())])
                except:
                    ret.append(self.visit(it))
        return ret

    @staticmethod
    def __return_object_creation__(self, return_object, var_name):
        if len(self.runningFunctions) > 0:
            if var_name is not None:
                last = self.runningFunctions[len(self.runningFunctions) - 1]
                last.variables[var_name] = return_object
            return return_object

        elif len(self.runningFunctions) == 0:
            if var_name is not None:
                last = self.variables
                last[var_name] = return_object
            return return_object

    @staticmethod
    def write(self, ctx: OrTexParser.FunctionCallContext):
        smth = self.visit(ctx.parameters())
        toPrint = ""

        if len(self.runningFunctions) > 0:
            for it in smth:
                varDict = self.runningFunctions[len(self.runningFunctions) - 1].variables
                try:
                    toPrint += str(varDict[str(it.IDENTIFIER())])
                except:
                    toPrint += str(self.visit(it))
        else:
            for it in smth:
                try:
                    toPrint += str(self.variables[str(it.IDENTIFIER())])
                except:
                    toPrint += str(self.visit(it))

        print(toPrint)

    @staticmethod
    def List(self, ctx: OrTexParser.ObjectCreationCallContext):
        args = SysFunction.__scan_args_object_creation__(self, ctx)

        if len(args) == 1:
            return SysFunction.__return_object_creation__(self, Cl.List(args[0]), args[0])
        elif len(args) == 0:
            return SysFunction.__return_object_creation__(self, Cl.List("InplaceCreation"), None)

    @staticmethod
    def Dict(self, ctx: OrTexParser.ObjectCreationCallContext):
        args = SysFunction.__scan_args_object_creation__(self, ctx)

        if len(args) == 1:
            return SysFunction.__return_object_creation__(self, Cl.Dict(args[0]), args[0])
        elif len(args) == 0:
            return SysFunction.__return_object_creation__(self, Cl.Dict("InplaceCreation"), None)

    @staticmethod
    def Space(self, ctx: OrTexParser.ObjectCreationCallContext):
        args = SysFunction.__scan_args_object_creation__(self, ctx)

        if len(args) == 3:
            return SysFunction.__return_object_creation__(self, Sp(args[0], args[1], args[2]), args[0])
        elif len(args) == 2:
            return SysFunction.__return_object_creation__(self, Sp("InplaceCreation", args[0], args[1]), None)
        else:
            print("space wrong size!")
            sys.exit(-1000)


class UserFunction:
    @staticmethod
    def referenceReturnFromUserDefinedFunction(self):
        if len(self.runningFunctions) > 1:
            current = self.runningFunctions[len(self.runningFunctions) - 1]
            last = self.runningFunctions[len(self.runningFunctions) - 2]
            for var in current.to_ret_reference.keys():
                last.variables[var] = current.variables[current.to_ret_reference[var]]

        elif len(self.runningFunctions) > 0:
            current = self.runningFunctions[len(self.runningFunctions) - 1]
            for var in current.to_ret_reference.keys():
                self.variables[var] = current.variables[current.to_ret_reference[var]]

    @staticmethod
    def returnFromUserDefinedFunction(self, function, ctx):
        if function.to_ret is None:
            if ctx.children[4].children is not None:
                sys.exit(-1000)
            return None
        else:
            name = function.to_ret
            var = function.variables[function.to_ret]
            toReturn = None
            next_f_calls = self.visit(ctx.objectFunctionCallFromFunction())
            objectTypes = self.objectTypes_
            entered = False

            for obj in objectTypes:
                try:
                    if var.type == obj[1].type:
                        # entered = True

                        if len(next_f_calls) != 0:
                            entered = True
                            var = var.methodCall(next_f_calls[0][0], next_f_calls[0][1])
                            toReturn = var.toReturn
                            next_f_calls.pop(0)

                        while len(next_f_calls) > 0:
                            var = self.__fromOFCall__(self, var, toReturn, next_f_calls, objectTypes)
                            toReturn = var.toReturn
                            next_f_calls.pop(0)

                        var.toReturn = None
                except:
                    if len(next_f_calls) != 0:
                        entered = True
                        toReturn = var

                    while len(next_f_calls) > 0:
                        var = self.__fromOFCall__(self, var, toReturn, next_f_calls, objectTypes)
                        toReturn = var.toReturn
                        next_f_calls.pop(0)

            if not entered:
                toReturn = var

            return toReturn

    @staticmethod
    def userDefinedFunction(self, ctx: OrTexParser.FunctionCallContext):
        name = str(ctx.IDENTIFIER())

        paramNames = []
        paramConst = []
        to_ret = {}
        for param in self.visit(ctx.parameters()):
            try:
                if '@' in str(param.IDENTIFIER()):
                    to_ret[str(param.IDENTIFIER()).replace("@", "")] = None
                    paramNames.append(str(param.IDENTIFIER()).replace("@", ""))
                else:
                    paramNames.append(str(param.IDENTIFIER()))
            except:
                paramNames.append("$")
                paramConst.append(param)

        i = 0
        j = 0
        for key in self.functions[name][1].keys():
            if i == len(paramNames):
                break
            if len(self.runningFunctions) > 0:
                if paramNames[i] != "$":
                    self.functions[name][1][key] = self.runningFunctions[len(self.runningFunctions) - 1].variables[
                        paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    self.functions[name][1][key] = self.visit(paramConst[j])
                    i += 1
                    j += 1
            else:
                if paramNames[i] != "$":
                    self.functions[name][1][key] = self.variables[paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    self.functions[name][1][key] = self.visit(paramConst[j])
                    i += 1
                    j += 1

        self.runningFunctions.append(
            Cl.Function(name, len(self.runningFunctions), deepcopy(self.functions[name][1]), to_ret,
                        self.functions[name][2]))

        self.visit(self.functions[str(ctx.IDENTIFIER())][0])

        return UserFunction.returnFromUserDefinedFunction(self, self.runningFunctions[len(self.runningFunctions) - 1], ctx)


class UserMethod:
    @staticmethod
    def referenceReturnFromUserDefinedMethod(self):
        if len(self.runningFunctions) > 1:
            current = self.runningFunctions[len(self.runningFunctions) - 1]
            last = self.runningFunctions[len(self.runningFunctions) - 2]
            for var in current.to_ret_reference.keys():
                last.variables[var] = current.variables[current.to_ret_reference[var]]

        elif len(self.runningFunctions) > 0:
            current = self.runningFunctions[len(self.runningFunctions) - 1]
            for var in current.to_ret_reference.keys():
                self.variables[var] = current.variables[current.to_ret_reference[var]]

    @staticmethod
    def returnFromUserDefinedMethod(self, function, ctx):
        if function.to_ret is None:
            if ctx.children[6].children is not None:
                sys.exit(-1000)
            return None
        else:
            name = function.to_ret
            var = function.variables[function.to_ret]
            toReturn = None
            next_f_calls = self.visit(ctx.objectFunctionCallFromFunction())
            objectTypes = self.objectTypes_
            entered = False

            for obj in objectTypes:
                try:
                    if var.type == obj[1].type:
                        # entered = True

                        if len(next_f_calls) != 0:
                            entered = True
                            var = var.methodCall(next_f_calls[0][0], next_f_calls[0][1])
                            toReturn = var.toReturn
                            next_f_calls.pop(0)

                        while len(next_f_calls) > 0:
                            var = self.__fromOFCall__(self, var, toReturn, next_f_calls, objectTypes)
                            toReturn = var.toReturn
                            next_f_calls.pop(0)

                        var.toReturn = None
                except:
                    if len(next_f_calls) != 0:
                        entered = True
                        toReturn = var

                    while len(next_f_calls) > 0:
                        var = self.__fromOFCall__(self, var, toReturn, next_f_calls, objectTypes)
                        toReturn = var.toReturn
                        next_f_calls.pop(0)

            if not entered:
                toReturn = var

            return toReturn

    @staticmethod
    def userDefinedMethod(self, method, ctx_):
        paramNames = []
        paramConst = []
        to_ret = {}
        for param in self.visit(ctx_.parameters()):
            try:
                if '@' in str(param.IDENTIFIER()):
                    to_ret[str(param.IDENTIFIER()).replace("@", "")] = None
                    paramNames.append(str(param.IDENTIFIER()).replace("@", ""))
                else:
                    paramNames.append(str(param.IDENTIFIER()))
            except:
                paramNames.append("$")
                paramConst.append(param)

        i = 0
        j = 0
        for key in method[1].keys():
            if i == len(paramNames):
                break
            if len(self.runningFunctions) > 0:
                if paramNames[i] != "$":
                    method[1][key] = self.runningFunctions[len(self.runningFunctions) - 1].variables[paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    method[1][key] = self.visit(paramConst[j])
                    i += 1
                    j += 1
            else:
                if paramNames[i] != "$":
                    method[1][key] = self.variables[paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    method[1][key] = self.visit(paramConst[j])
                    i += 1
                    j += 1

        self.runningFunctions.append(Cl.Function(ctx_.children[2], len(self.runningFunctions), deepcopy(method[1]), to_ret, method[2]))

        self.visit(method[0])

        return UserMethod.returnFromUserDefinedMethod(self, self.runningFunctions[len(self.runningFunctions) - 1], ctx_)

    @staticmethod
    def userConstructor(self, ctx: OrTexParser.objectCreationCall):
        className = str(ctx.IDENTIFIER())

        paramNames = []
        paramConst = []
        to_ret = {}
        for param in self.visit(ctx.parameters()):
            try:
                if '@' in str(param.IDENTIFIER()):
                    to_ret[str(param.IDENTIFIER()).replace("@", "")] = None
                    paramNames.append(str(param.IDENTIFIER()).replace("@", ""))
                else:
                    paramNames.append(str(param.IDENTIFIER()))
            except:
                paramNames.append("$")
                paramConst.append(param)

        i = 0
        j = 0
        fields = self.classes[className].constructor[1]
        for key in fields.keys():
            if i == len(paramNames):
                break
            if len(self.runningFunctions) > 0:
                if paramNames[i] != "$":
                    fields[key] = self.runningFunctions[len(self.runningFunctions) - 1].variables[paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    fields[key] = self.visit(paramConst[j])
                    i += 1
                    j += 1
            else:
                if paramNames[i] != "$":
                    fields[1][key] = self.variables[paramNames[i]]
                    if paramNames[i] in to_ret.keys():
                        to_ret[paramNames[i]] = key
                    i += 1
                else:
                    fields[key] = self.visit(paramConst[j])
                    i += 1
                    j += 1

        self.runningFunctions.append(Cl.Function(className, len(self.runningFunctions), fields, to_ret, None))

        self.visit(self.classes[className].constructor[0])
