from antlr4 import *
from MyListener import MyListener
from patitoLexer import patitoLexer
from patitoParser import patitoParser

def main():
    input_stream = FileStream("example2.patito")
    lexer = patitoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = patitoParser(stream)

    tree = parser.startRule()

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
