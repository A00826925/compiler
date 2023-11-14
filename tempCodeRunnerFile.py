("example.patito")
    lexer = patitoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = patitoParser(stream)

    tree = parser.startRule()

    listener = MyListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()
