import sys
from antlr4 import *
from patitoLexer import patitoLexer
from patitoParser import patitoParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = patitoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = patitoParser(stream)
    tree = parser.startRule()

if __name__ == '__main__':
    main(sys.argv)