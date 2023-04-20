import sys
from os import path

from OrTex.ErrorHandler import ErrorHandler
from OrTex.MyVisitor import MyVisitor
from antlr4 import *
from OrTex.OrTex.OrTexLexer import OrTexLexer
from OrTex.OrTex.OrTexParser import OrTexParser

# in: "komp22-ortex" use: "antlr -Dlanguage=Python3 .\OrTex\OrTex.g4 -visitor -o .\OrTex" -> update grammar
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You should have specified one file to be interpreted!")
        sys.exit(-1000)

    if not path.exists(sys.argv[1]):
        print("You should have specified path to existing file!")
        sys.exit(-1000)

    if '.' not in sys.argv[1]:
        print("You should have specified path to existing .ot file!")
        sys.exit(-1000)

    if sys.argv[1].split('.')[len(sys.argv[1].split('.')) - 1] != "ot":
        print("You should have specified path to existing .ot file! Fix your Extension!")
        sys.exit(-1000)

    data = FileStream(sys.argv[1], encoding='utf-8')

    # lexer
    lexer = OrTexLexer(data)
    stream = CommonTokenStream(lexer)

    # parser
    parser = OrTexParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        sys.exit(-1000)

    # evaluator
    visitor = MyVisitor()
    visitor.visit(tree)

    # start program from main if exists
    if visitor.startPoint is not None:
        print("$$START$$")
        a = visitor.visit(visitor.startPoint)
        print("$$DONE$$")
    else:
        ErrorHandler.NoMainFunction(visitor)
    print('Press anything to terminate.')
    input()
