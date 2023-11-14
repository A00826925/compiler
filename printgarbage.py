def printgarbage(parser, vars_table):
    print("Vars Table:")
    for var, var_type in vars_table.items():
        print(f"{var}: {var_type}")
