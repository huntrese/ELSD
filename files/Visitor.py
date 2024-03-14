from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser
from HelloVisitor import HelloVisitor

# Custom visitor class
class MyVisitor(HelloVisitor):
    def visitR(self, ctx):
        print("Visiting R node")

    def visitDiabetesData(self, ctx):
        print("Visiting DiabetesData node")

    # Implement other visit methods as needed


def main():
    # Input string to parse
    input_string = "diabetesData; r;"

    # Create a lexer and parser
    lexer = HelloLexer(InputStream(input_string))
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)

    # Parse the input to generate a parse tree
    parse_tree = parser.start_()
    # Create an instance of your visitor class
    visitor = MyVisitor()

    # Traverse the parse tree using your visitor instance
    visitor.visit(parse_tree)


if __name__ == '__main__':
    main()
