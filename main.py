import sys
from antlr4 import *
from files.HelloLexer import HelloLexer
from files.HelloParser import HelloParser


def main(argv):
     input = FileStream(argv[1])
    lexer = HelloLexer(input)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)