import copy
import enum
import sys


class Function:
    def __init__(self, name, fun_id, variables, to_ret_reference, to_ret):
        self.name = name
        self.funId = fun_id
        self.variables = variables
        self.to_ret_reference = to_ret_reference
        self.to_ret = to_ret


class Scope:
    def __init__(self, index):
        self.variables = []
        self.index = index
        self.name = "_##SCOPE##_" + str(self.index)


class List:
    def __init__(self, name):
        self.name = name
        self.type = "List"
        self.toReturn = None
        self.list = list()

    class FNames(enum.Enum):
        pushF = 1
        pushB = 2
        popF = 3
        popB = 4
        clear = 5
        get = 6
        set = 7
        size = 8

    def __str__(self):
        return str(self.list)

    def methodCall(self, method_name, args):
        for fName in self.FNames:
            if fName.name == method_name:
                doSomething = getattr(self, "__" + method_name + "__")
                return doSomething(args)

    def __pushB__(self, args):
        for item in args:
            try:
                newItem = copy.deepcopy(item)
                self.list.append(newItem)
                self.toReturn = self
            except:
                newItem = Object(item.class_type, item.fields, item.methods)
                self.list.append(newItem)
                self.toReturn = self
        return self

    def __pushF__(self, args):
        for item in args:
            self.list.insert(0, item)
            self.toReturn = self
        return self

    def __popF__(self, args):
        if len(args) == 0:
            self.toReturn = self.list.pop(0)
            return self

    def __popB__(self, args):
        if len(args) == 0:
            self.toReturn = self.list.pop()
            return self

    def __clear__(self, args):
        if len(args) == 0:
            self.list.clear()
            self.toReturn = self
            return self

    def __get__(self, args):
        if len(args) == 1:
            self.toReturn = self.list[args[0]]
            return self
        if len(args) == 2:
            self.toReturn = self.list[args[0]].list[args[1]]
            return self

    def __set__(self, args):
        if len(args) == 2:
            self.list[args[0]] = args[1]
            self.toReturn = self
            return self
        if len(args) == 3:
            self.list[args[0]].list[args[1]] = args[2]
            self.toReturn = self
            return self

    def __size__(self, args):
        if len(args) == 0:
            self.toReturn = len(self.list)
            return self


class Dict:
    def __init__(self, name):
        self.name = name
        self.type = "Dict"
        self.toReturn = None
        self.dict = dict()

    class FNames(enum.Enum):
        clear = 1
        get = 2
        set = 3
        add = 4
        delete = 5
        size = 6

    def __str__(self):
        return str(self.dict)

    def methodCall(self, method_name, args):
        for fName in self.FNames:
            if fName.name == method_name:
                doSomething = getattr(self, "__" + method_name + "__")
                return doSomething(args)

    def __clear__(self, args):
        if len(args) == 0:
            self.dict.clear()
            self.toReturn = self
        return self

    def __get__(self, args):
        if len(args) == 1:
            if args[0] in self.dict.keys():
                self.toReturn = self.dict[args[0]]
        return self

    def __set__(self, args):
        if len(args) == 2:
            self.dict[args[0]] = args[1]
            self.toReturn = self
        return self

    def __add__(self, args):
        if len(args) == 2:
            try:
                newItem = copy.deepcopy(args[1])
                self.dict[args[0]] = newItem
                self.toReturn = self
            except:
                newItem = Object(args[1].class_type, args[1].fields, args[1].methods)
                self.dict[args[0]] = newItem
                self.toReturn = self
        return self

    def __delete__(self, args):
        for item in args:
            if item in self.dict.keys():
                self.dict.pop(item)
            else:
                sys.exit(-1000)
        self.toReturn = self
        return self

    def __size__(self, args):
        if len(args) == 0:
            self.toReturn = len(self.dict)
        else:
            sys.exit(-1000)
        return self


class Class:
    def __init__(self, class_type, class_id, fields, methods, constructor):
        self.class_type = class_type
        self.class_id = class_id
        self.fields = fields
        self.methods = methods
        self.constructor = constructor


class Object:
    def __init__(self, class_type, fields, methods):
        self.class_type = class_type
        self.fields = fields
        self.methods = methods
        self.toReturn = None


class Interface:
    pass


class Enum:
    pass
