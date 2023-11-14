grammar patito;

@parser::header {

from varfunctable import *
global funclist, quads
funclist = FuncTable()
quads = Cuadruplos()

global current_content, current_func, current_scope, current_type, current_var, various_vars, temporal_operator

current_var = ''
current_func = ''
current_type = ''
current_scope = 0
current_content = ''
various_vars = []
temporal_operator = ''

}


startRule : programa EOF;

programa : 'program'{quads.quad_main_init()} Id {global current_func, current_scope; current_func = $Id.text; funclist; funclist.add_function($Id.text)}
';' (vars? funcs* 
'main'{quads.quad_main_set()} {current_scope+=1; 
current_func = "main";
funclist.add_function(current_func)} 
body {current_scope-=1}
'end' {funclist.print_all_functions(); quads.printQuads()});
vars : {global current_content, current_func, current_scope, current_type, current_var, various_vars}
'var' (Id {various_vars.append($Id.text)} (',' Id {various_vars.append($Id.text)})* ':' type {current_type = $type.text} ';'{
for myvar in various_vars: funclist.add_variable_to_function(current_func, myvar, current_type, current_scope, current_content);
various_vars = [];
})+; 
type : 'int' | 'float';
funcs : {global current_content, current_func, current_scope, current_type, current_var} 
'void' {current_scope+=1} Id {current_func = $Id.text; funclist.add_function(current_func)}
'(' (Id ':' type 
{current_var = $Id.text; 
current_type = $type.text; 
funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)}
(',' Id ':' type 
{current_var = $Id.text; current_type = $type.text; 
funclist.add_variable_to_function(current_func, current_var, current_type, current_scope, current_content)}
)*)* ')' '[' vars? body ']' ';'
{current_scope-=1;}
{funclist.delete_all_variables(current_func)};
body : '{' (statement)* '}';
statement : assign | condition | cycle | f_call | print;
assign : Id {
quads.push_operate(funclist.get_variable_memory($Id.text, current_scope), funclist.get_variable_type($Id.text, current_scope), False, False, 0, '')
} '=' {
quads.push_operator('=')
}expression {
quads.quads_Assign()
}';';
expression : exp {
quads.quads_Compare()
}(('>' {
quads.push_operator('>')
}| '<' {
quads.push_operator('<')
}| '!='{
quads.push_operator('!=')
}) exp{
quads.quads_Compare()
})*;
exp : termino {
quads.quads_PlusMin()
}(('+' {
quads.push_operator('+')
}| '-'{
quads.push_operator('-')
}) termino{
quads.quads_PlusMin()
})*;
termino : factor {
quads.quads_MultDiv()
}(('*' {
quads.push_operator('*')
}| '/'{
quads.push_operator('/')
}) factor{
quads.quads_MultDiv()
})*;
factor : ('(' {
quads.push_FF()
}expression ')'{
quads.pop_FF()
}) | ({global temporal_operator}('+' {temporal_operator = '+'}| '-' {temporal_operator = '-'}) (Id {
quads.push_operate(funclist.get_variable_memory($Id.text, current_scope), funclist.get_variable_type($Id.text, current_scope), False, False, $Id.text, temporal_operator); temporal_operator = ''
} | cte)) | (Id{
quads.push_operate(funclist.get_variable_memory($Id.text, current_scope), funclist.get_variable_type($Id.text, current_scope), False, False, $Id.text, '')
} | cte);
Id : [a-zA-Z][a-zA-Z0-9]*;
cte : Cte_int{global temporal_operator}{
quads.push_operate($Cte_int.text, "int", True, False, 0, temporal_operator); temporal_operator = ''
}| Cte_float {
quads.push_operate($Cte_float.text, "float", True, False, 0, temporal_operator); temporal_operator = ''
}| Cte_string {
quads.push_operate($Cte_string.text, "string", True, False, 0, temporal_operator); temporal_operator = ''
};
Cte_int : [0-9]+;
Cte_float : [0-9]+ '.' [0-9]+;
Cte_string : '"' .*? '"';
condition : 'if' '(' expression')'{
quads.quad_if_1()
}
body ('else' {
quads.quad_if_3()
} body)? ';'{
quads.quad_if_2()
};
cycle : 'while' {
quads.quad_while_1()
} body 'do' '(' expression ')'{
quads.quad_while_return()
} ';'{

};
f_call : Id '(' (expression (',' expression)*)? ')' ';';
print : 'print' {
quads.push_operator('print')
}'(' (Cte_string {
quads.push_operate($Cte_string.text, "string", True, False, 0, '')
}| expression) (',' (Cte_string {
quads.push_operate($Cte_string.text, "string", True, False, 0, '')
}| expression))* ')'{
quads.quads_Print()
} ';';

WS : [ \t\r\n]+ -> skip;
