from vmach import *
global virtualM
virtualM = VM()

vgi = 1000 #int
vgf = 2000 #float
vli = 3000 #int
vlf = 4000 #float
ti = 5000 #int
tf = 6000 #float
tb = 7000 #bool
ci = 8000 #int
cf = 9000 #float
cs = 10000 #bool

operator_dict = {
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
}

inverse_operator_dict = {
    1: '+',
    2: '-',
    3: '*',
    4: '/',
    5: '<',
    6: '>',
    7: '==',
    8: '!=',
    9: '<=',
    10: '>=',
    11: '(',
    12: ')',
    13: 'if',
    14: 'else',
    15: '=',
    16: 'print',
    17: 'GoToF',
    18: 'GoTo',
    19: 'GoToV'
}

mem_dict = {}
operand_dict = {}
QUADS = []

class Cuadruplos:
    def __init__(self):
        self.stack_operators = []
        self.stack_operand = []
        self.stack_types = []
        self.stack_jump = []
    def semantics(self, left_type, right_type, operator):
        global inverse_operator_dict
        operator_final = inverse_operator_dict[operator]
        print(operator_final)
        cube = {
            ('int', 'int', '+'): 'int',
            ('int', 'int', '-'): 'int',
            ('int', 'int', '/'): 'float',
            ('int', 'int', '*'): 'int',
            ('float', 'int', '+'): 'float',
            ('float', 'int', '-'): 'float',
            ('float', 'int', '/'): 'float',
            ('float', 'int', '*'): 'float',
            ('float', 'float', '+'): 'float',
            ('float', 'float', '-'): 'float',
            ('float', 'float', '/'): 'float',
            ('float', 'float', '*'): 'float',
            ('int', 'float', '+'): 'float',
            ('int', 'float', '-'): 'float',
            ('int', 'float', '/'): 'float',
            ('int', 'float', '*'): 'float',
            ('bool', 'bool', '&'): 'bool',

            ('int', 'int', '>'): 'bool',
            ('int', 'int', '<'): 'bool',
            ('float', 'float', '>'): 'bool',
            ('float', 'float', '<'): 'bool',
            ('float', 'int', '>'): 'bool',
            ('float', 'int', '<'): 'bool',
            ('int', 'float', '>'): 'bool',
            ('int', 'float', '<'): 'bool',
            ('bool', 'bool', '>'): 'bool',
            ('bool', 'bool', '<'): 'bool',
            ('int', 'bool', '>'): 'bool',
            ('int', 'bool', '<'): 'bool',
            ('float', 'bool', '>'): 'bool',
            ('float', 'bool', '<'): 'bool',
            ('bool', 'int', '>'): 'bool',
            ('bool', 'int', '<'): 'bool',
            ('bool', 'float', '>'): 'bool',
            ('bool', 'float', '<'): 'bool',


            ('int', 'int', '=='): 'bool',
            ('float', 'float', '=='): 'bool',
            ('bool', 'bool', '=='): 'bool',
            ('int', 'float', '=='): 'bool',
            ('float', 'int', '=='): 'bool',

            ('int', 'int', '!='): 'bool',
            ('float', 'float', '!='): 'bool',
            ('bool', 'bool', '!='): 'bool',
            ('int', 'float', '!='): 'bool',
            ('float', 'int', '!='): 'bool',

            ('int', 'int', '<='): 'bool',
            ('float', 'float', '<='): 'bool',
            ('bool', 'bool', '<='): 'bool',
            ('int', 'float', '<='): 'bool',
            ('float', 'int', '<='): 'bool',

            ('int', 'int', '>='): 'bool',
            ('float', 'float', '>='): 'bool',
            ('bool', 'bool', '>='): 'bool',
            ('int', 'float', '>='): 'bool',
            ('float', 'int', '>='): 'bool',
        }

        return cube.get((left_type, right_type, operator_final), 'err')

    def push_operator(self, operator):
        self.stack_operators.append(operator_dict[operator])
        print(self.stack_operators)

    def push_operate(self, operand, type, isConst, isTemp, optional, simbolo):
        global ci, cf, cs, tf, ti, tb
        if isConst and not operand_dict.get(operand, False):
            if type == "int": operand_dict[operand] = ci; mem_dict[ci] = operand; ci+=1
            elif type == "float": operand_dict[operand] = cf; mem_dict[cf] = operand; cf+=1
            elif type == "string": operand_dict[operand] = cs; mem_dict[cs] = operand; cs+=1
            if simbolo == "-":
                self.stack_operand.append(operand_dict[operand]*-1)
            else:
                self.stack_operand.append(operand_dict[operand])
            self.stack_types.append(type)
            print(mem_dict)
        elif isConst and isTemp and not operand_dict.get(operand, False):
            if type == "int": operand_dict[operand] = ti; mem_dict[ti] = operand; ti+=1
            elif type == "float": operand_dict[operand] = tf; mem_dict[tf] = operand; tf+=1
            elif type == "bool": operand_dict[operand] = tb; mem_dict[tb] = operand; tb+=1
            self.stack_operand.append(operand_dict[operand])
            self.stack_types.append(type)
        elif isConst and operand_dict.get(operand, False):
            mem_dict[operand_dict[operand]] = operand
            if simbolo == "-":
                self.stack_operand.append(operand_dict[operand]*-1)
            else:
                self.stack_operand.append(operand_dict[operand])
            self.stack_types.append(type)
        elif not isConst:
            print("pushed: ", operand, " = ", type)
            if simbolo == "-":
                new = operand * -1
            else:
                new = operand
            mem_dict[operand] = optional
            self.stack_operand.append(new)
            self.stack_types.append(type)

    def push_FF(self):
        self.stack_operators.append(operator_dict['('])

    def pop_FF(self):
        self.stack_operators.pop()

    def pop_operator(self):
        return self.stack_operators.pop() if self.stack_operators else None

    def pop_operand(self):
        return self.stack_operand.pop() if self.stack_operand else None

    def pop_type(self):
        return self.stack_types.pop() if self.stack_types else None
    
    def pop_jump(self):
        return self.stack_jump.pop() if self.stack_jump else None
    
    def quads_Compare(self):
        global QUADS, tf, ti, tb
        print("not entered compare with: ", self.stack_operators, "and ", self.stack_operand)
        if len(self.stack_operators) > 0 and (self.stack_operators[-1] == operator_dict['>'] or self.stack_operators[-1] == operator_dict['<'] or self.stack_operators[-1] == operator_dict['<='] or self.stack_operators[-1] == operator_dict['>='] or self.stack_operators[-1] == operator_dict['=='] or self.stack_operators[-1] == operator_dict['!=']):
            print("entered compare with: ", self.stack_operators, "and ", self.stack_operand)
            right_operand = self.pop_operand()
            right_type = self.pop_type()
            left_operand = self.pop_operand()
            left_type = self.pop_type()
            operator = self.pop_operator()

            result_type = self.semantics(left_type, right_type, operator)

            if result_type == 'int': new_temp = ti; ti+=1
            elif result_type == 'float': new_temp = tf; tf+=1
            elif result_type == 'bool': new_temp = tb; tb+=1
            else: print(left_type, left_operand, right_type, right_operand, operator); raise TypeError('error')

            quad = (operator, left_operand, right_operand, new_temp)
            mem_dict[new_temp] = 0
            self.stack_operand.append(new_temp)
            self.stack_types.append(result_type)

            QUADS.append(quad)

    def quads_PlusMin(self):
        global QUADS, tf, ti, tb
        if len(self.stack_operators) > 0 and (self.stack_operators[-1] == operator_dict['+'] or self.stack_operators[-1] == operator_dict['-']):
            right_operand = self.pop_operand()
            right_type = self.pop_type()
            left_operand = self.pop_operand()
            left_type = self.pop_type()
            operator = self.pop_operator()

            result_type = self.semantics(left_type, right_type, operator)

            if result_type == 'int': new_temp = ti; ti+=1
            elif result_type == 'float': new_temp = tf; tf+=1
            elif result_type == 'bool': new_temp = tb; tb+=1
            else: raise TypeError('error')

            quad = (operator, left_operand, right_operand, new_temp)
            self.stack_operand.append(new_temp)
            mem_dict[new_temp] = 0
            self.stack_types.append(result_type)

            QUADS.append(quad)

    def quads_MultDiv(self):
        global QUADS, tf, ti, tb
        if len(self.stack_operators) > 0 and (self.stack_operators[-1] == operator_dict['*'] or self.stack_operators[-1] == operator_dict['/']):
            right_operand = self.pop_operand()
            right_type = self.pop_type()
            left_operand = self.pop_operand()
            left_type = self.pop_type()
            operator = self.pop_operator()

            result_type = self.semantics(left_type, right_type, operator)

            if result_type == 'int': new_temp = ti; ti+=1
            elif result_type == 'float': new_temp = tf; tf+=1
            elif result_type == 'bool': new_temp = tb; tb+=1
            else: raise TypeError('error')

            quad = (operator, left_operand, right_operand, new_temp)
            self.stack_operand.append(new_temp)
            mem_dict[new_temp] = 0
            self.stack_types.append(result_type)

            QUADS.append(quad)

    def quads_Assign(self):
        global QUADS
        if len(self.stack_operators) > 0 and (self.stack_operators[-1] == operator_dict['=']):
            print("entered assign")
            right_operand = self.pop_operand()
            right_type = self.pop_type()
            left_operand = self.pop_operand()
            left_type = self.pop_type()
            operator = self.pop_operator()

            result_type = self.semantics(left_type, right_type, operator)
            quad = (operator, right_operand, None, left_operand)
            QUADS.append(quad)

    def quads_Print(self):
        global QUADS
        if len(self.stack_operators) > 0 and (self.stack_operators[-1] == operator_dict['print']):
            print("entered assign")
            right_operand = self.pop_operand()
            right_type = self.pop_type()
            operator = self.pop_operator()

            quad = (operator, None, None, right_operand)
            QUADS.append(quad)
    
    def quad_if_1(self):
        global QUADS
        type = self.pop_type()


        print(type)
        if type != 'bool': raise TypeError("TYPE MISMATCH")
        else:
            operand = self.pop_operand()
            quad = (17, operand, None, None)
            QUADS.append(quad)
            self.stack_jump.append(len(QUADS)-1)
    
    def quad_if_2(self):
        global QUADS
        
        pos_jump_end = self.pop_jump()
        quad = QUADS[pos_jump_end]
        new_quad = quad[:3] + (len(QUADS),)
        QUADS[pos_jump_end] = new_quad

    def quad_if_3(self):
        global QUADS
        

        quad = (18, None, None, None)
        QUADS.append(quad)

        cont = len(QUADS)
        pos_jump_false = self.pop_jump()
        self.stack_jump.append(cont-1)
        quad = QUADS[pos_jump_false]
        new_quad = quad[:3] + (cont,)
        QUADS[pos_jump_false] = new_quad


    def quad_while_1(self):
        global QUADS
        self.stack_jump.append(len(QUADS))

    def quad_while_2(self):
        global QUADS

        type = self.pop_type()
        if type != 'bool': raise TypeError("TYPE MISMATCH")
        else:
            operand = self.pop_operand()
            quad = (17, operand, None, None)
            QUADS.append(quad)
            self.stack_jump.append(len(QUADS)-1)

    def quad_while_3(self):
        global QUADS

        end = self.pop_jump()
        back = self.pop_jump()

        quad = (18, None, None, back)
        QUADS.append(quad)

        quad = QUADS[end]
        quad[3] = len(QUADS)
    
    def quad_while_return(self):
        global QUADS

        type = self.pop_type()
        if type != 'bool': raise TypeError("TYPE MISMATCH")
        else:
            ret = self.pop_jump()
            result = self.pop_operand()
            print("resultado while: ", result)
            quad = (19, result, None, ret)
            QUADS.append(quad)

    def quad_main_init(self):
        global QUADS

        quad = (18, None, None, None)
        QUADS.append(quad)

    def quad_main_set(self):
        global QUADS

        jumpto = len(QUADS)
        if jumpto == 0:
            jumpto = 1

        QUADS[0] = (18, None, None, jumpto)

    def printQuads(self):
        global QUADS
        print(QUADS)
        virtualM.Order66(mem_dict, inverse_operator_dict, QUADS)


class VarTable:
    def __init__(self):
        self.variables = {}

    def add_variable(self, name, type, scope, content):
        global vgi, vgf, vli, vlf
        current_memory = 0

        if scope != 0:
            if type == "int":
                current_memory = vli
                vli+=1
            else:
                current_memory = vlf
                vlf+=1
        else:
            if type == "int":
                current_memory = vgi
                vgi+=1
            else:
                current_memory = vgf
                vgf+=1

        if name not in self.variables:
            self.variables[name] = {'type': type, 'scope': scope, 'content': content, 'memory': current_memory}
            print(f"variable '{name}' scope '{scope}'added successfully")
        else:
            print(f"variable '{name}' already exists")

    def search_variable(self, name):
        if name in self.variables:
            return self.variables[name]
        else:
            return None
        
    def delete_variable(self, name):
        if name in self.variables:
            del self.variables[name]
            print(f"variable '{name}' deleted successfully")
        else:
            print(f"variable '{name}' not found")

    def delete_all_variables(self):
        self.variables = {}
        print("all variables deleted successfully")
    


class FuncTable:
    def __init__(self):
        self.functions = {}

    def add_function(self, name):
        if name not in self.functions:
            self.functions[name] = VarTable() #add VARTABLE to new FUNCTION
            print(f"function '{name}' added successfully")
        else:
            print(f"function '{name}' already exists")

    def add_variable_to_function(self, func, var, type, scope, content):
        if func in self.functions:
            # check for both name and scope, after, if scope check passes, will check for name in same function on the var calss
            existing_variable = self.search_variable_in_functions(var, scope)
            if existing_variable:
                print(f"variable '{var}' already exists in parent")
            else:
                self.functions[func].add_variable(var, type, scope, content)
        else:
            print(f"function '{func}' not found")

    def get_variable_type(self, var, scope):
        existing_variable = self.search_variable_in_functions(var, scope)
        if existing_variable:
            return existing_variable['type']
        else:
            raise ValueError(f"Variable '{var}' not found in function with scope {scope}")

    def get_variable_memory(self, var, scope):
        existing_variable = self.search_variable_in_functions(var, scope)
        if existing_variable:
            return existing_variable['memory']
        else:
            raise ValueError(f"Variable '{var}' not found in function with scope {scope}")

    def search_variable_in_functions(self, var, scope):
        for func, var_table in self.functions.items():
            existing_variable = var_table.search_variable(var)
            if existing_variable and (existing_variable['scope'] < scope or existing_variable['scope'] != 0):
                return existing_variable
        return None
        
    def print_all_functions(self):
        print("Functions:")
        for func, var_table in self.functions.items():
            print(f"- {func}:")
            for var, var_data in var_table.variables.items():
                print(f"  - {var}: {var_data['type']}, {var_data['scope']}, {var_data['content']}, {var_data['memory']}")

    def delete_function(self, func):
        if func in self.functions:
            del self.functions[func]
            print(f"funtion '{func}' deleted successfully")
        else:
            print(f"function '{func}' not found")

    def delete_all_variables(self, func):
        if func in self.functions:
            self.functions[func].delete_all_variables()
            print(f"all variables in function '{func}' deleted successfully")
        else:
            print(f"function '{func}' not found. from delallvars")
