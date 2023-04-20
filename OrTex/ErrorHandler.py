import sys


class ErrorHandler:
    @staticmethod
    def __programEnding__(visitor):
        visitor.__errorAtLine__()
        sys.exit(-1000)

    @staticmethod
    def variableDontExistInScope(visitor, name):
        print(F"name: {name} not in variables!")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def variableDontExistInFunctionScope(visitor, name):
        print(F"name: {name} not in function variables!")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def stringIsNotAvailable(visitor, name):
        print(F"String name: {name} is reserved.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def noSuchIncrement(visitor):
        print("Such incrementation operation doesn't exist.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def functionUsedOnBaseTypeObject(visitor, to_return_type):
        print(F"Cant use function on: {to_return_type} object!")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def noSuchConstant(visitor):
        print("Constant type is unknown.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def MultiplicationTypeFault(visitor):
        print("Types in multiplication operation doesn't match.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def DivisionBy0(visitor):
        print("You Cant divide by 0!")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def ComparisonTypesFault(visitor):
        print("Variables types in comparison operation doesn't match.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def FunctionExists(visitor, name):
        print(f"Function named: {name} already exists.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def FunctionMainFault(visitor):
        print("There can be only one MAIN function.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def FunctionNotExists(visitor, name):
        print(f"There is no function named: {name}.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def WrongBoolOperator(visitor):
        print("You used wrong boolean operator.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def AddingBool(visitor):
        print("Additive operations are not available for boolean values.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def MultiplicationBool(visitor):
        print("You can't perform multiplication operations on boolean values.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def NoMainFunction(visitor):
        print("There is no Main function to start the program.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def AddingNone(visitor):
        print("Additive operations are not available for NONE values.")
        ErrorHandler.__programEnding__(visitor)

    @staticmethod
    def MultiplicationNone(visitor):
        print("Multiplication operations are not available for NONE values.")
        ErrorHandler.__programEnding__(visitor)
