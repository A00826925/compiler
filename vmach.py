class VM:
    def Order66(self, mem_dict, operator_dict, QUADS):
        variable_types = {
            1000: int,  # vgi - int
            2000: float,  # vgf - float
            3000: int,  # vli - int
            4000: float,  # vlf - float
            5000: int,  # ti - int
            6000: float,  # tf - float
            7000: bool,  # tb - bool
            8000: int,  # ci - int
            9000: float,  # cf - float
            10000: str  # cs - string
        }
        print("hi!")
        print(mem_dict)
        print(operator_dict)
        cont = 0
        while cont < len(QUADS):
            quad = QUADS[cont]
            action = operator_dict[quad[0]]
            """
                '+': 1,
                '-': 2,
                '*': 3,
                '/': 4,
                '<': 5,
                '>': 6,
                '==': 7,
                '!=': 8,
                '<=': 9,
                '>=': 10,
                '(': 11,
                ')': 12,
                'if': 13,
                'else': 14,
                '=': 15,
                'print': 16,
                'GoToF': 17,
                'GoTo': 18,
                'GoToV': 19
            """
            if action == "+":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)

                mem_dict[quad[3]] = var1 + var2

                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "-":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)

                mem_dict[quad[3]] = var1 - var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "*":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 * var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "/":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                if var2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")           
                mem_dict[quad[3]] = var1 / var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "<":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 < var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == ">":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 > var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "==":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 == var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "!=":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 != var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "<=":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 <= var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == ">=":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                type_2 = variable_types[abs(quad[2]) // 1000 * 1000]

                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)
                var2 = type_2(mem_dict[abs(quad[2])]) * (-1 if quad[2] < 0 else 1)
                mem_dict[quad[3]] = var1 >= var2
                print("LALALA",var1, " ", action, " ", var2, " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "(":

                cont+=1
                pass
            elif action == ")":

                cont+=1
                pass
            elif action == "if":
                cont+=1
                pass
            elif action == "else":
                cont+=1
                pass
            elif action == "=":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                var1 = type_1(mem_dict[abs(quad[1])]) * (-1 if quad[1] < 0 else 1)

                mem_dict[abs(quad[3])] = var1
                print("LALALA",var1, " ", action, " ", " = ", mem_dict[abs(quad[3])])
                cont+=1
                pass
            elif action == "print":
                type_1 = variable_types[abs(quad[3]) // 1000 * 1000]
                var1 = type_1(mem_dict[abs(quad[3])])

                print("LALALA",var1, " ", action, " ", " = ", mem_dict[abs(quad[3])])
                print(var1)
                cont+=1
                pass
            elif action == "GoToF":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                var1 = type_1(mem_dict[abs(quad[1])])
                #print("LALALA",var1, " ", action, " ", " = ", mem_dict[abs(quad[3])])
                print('BBBB', var1)
                jump = int(abs(quad[3]))
                if var1:
                    cont+=1
                else:
                    cont = jump
                pass
            elif action == "GoTo":
                print(quad)
                jump = int(abs(quad[3]))
                cont = jump
                pass
            elif action == "GoToV":
                type_1 = variable_types[abs(quad[1]) // 1000 * 1000]
                var1 = type_1(mem_dict[abs(quad[1])]) 
                #print("LALALA",var1, " ", action, " ", " = ", mem_dict[abs(quad[3])])
                jump = int(abs(quad[3]))
                if var1:
                    cont = jump
                else:
                    cont +=1
                print("gotov", var1)
                pass
            # Add more elif statements for additional operators if needed
            else:
                # Handle the case where the operator is not recognized
                print(f"Operator '{action}' not recognized.")

