grammar baby_duck;

@parser::header {
from symbol_table import *
symbol_table1 = SymbolTable()
current_scope = 0

def infer_data_type(expression):
    if expression.isdigit():
        return 'int'
    try:
        float(expression)
        return 'float'
    except ValueError:
        return 'string'
}

@parser::members {


}

programRule : program EOF;

programa : 'program';
Id : [a-zA-Z]+[0-9]*;
main : 'main';
end : 'end';
var : 'var';
void : 'void';
int : 'int';
float : 'float';
else: 'else';
if : 'if';
while : 'while';
do : 'do';
CTE_STRING : '"'.*?'"';
CTE_INT : [0-9]+;
CTE_FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;

expression: exp (('>' | '<') exp | '!=' exp)*;
exp : term ('+' term | '-' term)*;
term: factor ('' factor | '/' factor);
factor: ('+'| '-')? (Id | CTE_INT | CTE_STRING | '(' expression ')');
body: '{' statement* '}';
assign: Id '=' expression ';';
condition: if '(' expression ')' body (else body)? ';';
cycle: while body do '(' expression ')' ';';
print: 'print' '(' (expression | CTE_STRING) (',' (expression | CTE_STRING))* ')' ';'{
symbol_table1.printSymbols();
symbol_table1.printFunctions();
};
functionCall: Id '(' (expression (',' expression)*)? ')' ';';
type: int | float;
variables: var listvars*;
listvars: listaId ':' type ';'{
symbol_table1.add_symbol($listaId.text, $type.text, current_scope);
};
listaId : Id idExtra;
idExtra : (',' listaId)?;
function: {global current_scope}void {current_scope+=1} Id '(' parameters* ')' '[' variables? body ']' ';'{
symbol_table1.add_function($Id.text, $parameters.text);
current_scope-=1;
symbol_table1.pop_function($Id.text);
};
parameters : parameter (',' parameter)*;

parameter: Id ':' type{
symbol_table1.add_symbol($Id.text, $type.text, current_scope)
};

program: programa Id ';' variables? (function)* main body end;
statement: (assign | condition | cycle | print | functionCall);