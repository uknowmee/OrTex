grammar OrTex;

program: (funDef | classDef | COMMENT)* EOF;

line: statement | ifStatement | whileStatement | forStatement | scope | COMMENT;

statement: (varDefinition | assignment | functionCall | objectFunctionCall | classMethodCall) ';';

ifStatement: 'if' '(' expression ')' block ('else' elseIfStatement)?;

elseIfStatement: block | ifStatement;

whileStatement: 'while' '(' expression ')' block;

forStatement: 'for' '(' assignment ',' expression ',' ('*' | '+' | '-') (IDENTIFIER | INTEGER) ')' block;

funDef: 'func' IDENTIFIER '(' parameters ')' block funDefReturn?;

funDefReturn: '->' IDENTIFIER ';';

parameters: (expression (',' expression)*)?;

assignment: IDENTIFIER '=' expression | classQuestion '=' expression;

varDefinition: IDENTIFIER | classQuestion;

functionCall: IDENTIFIER '(' parameters ')' objectFunctionCallFromFunction;

objectFunctionCall: IDENTIFIER '.'IDENTIFIER '(' parameters ')' objectFunctionCallFromFunction;

objectFunctionCallFromFunction: ('.'IDENTIFIER '(' parameters ')')*;

objectCreationCall: 'new' IDENTIFIER '(' parameters ')';

classDef: 'class' IDENTIFIER '{' classConstructor classMethodDef* '}';

classConstructor: 'constr' '(' parameters ')' block;

classMethodDef: 'func' IDENTIFIER '(' parameters ')' block funDefReturn?;

classQuestion: IDENTIFIER '.'IDENTIFIER;

classMethodCall: IDENTIFIER '.'IDENTIFIER '(' parameters ')' classMethodCallFromMethod;

classMethodCallFromMethod: ('.'IDENTIFIER '(' parameters ')')*;

inplaceQuestion: '.'IDENTIFIER;

expression
    : constant                                   #constantExpression
    | IDENTIFIER                                 #identifierExpression
    | functionCall inplaceQuestion?              #functionExpression
    | objectFunctionCall inplaceQuestion?        #objectFunctionCallExpression
    | objectCreationCall                         #objectCreationCallExpression
    | classQuestion                              #classQuestionExpression
    | classMethodCall                            #classMethodCallExpression
    | '(' expression ')'                         #parenthesizedExpression
    | '!' expression                             #notExpression
    | expression multOp expression               #multiplicativeExpression
    | expression addOp expression                #additiveExpression
    | expression compareOp expression            #comparisonExpression
    | expression boolOp expression               #booleanExpression
    ;

multOp: '*' | '/' | '%';
addOp: '+' | '-';
compareOp: '==' | '!=' | '>' | '<' | '>=' | '<=';
boolOp: BOOL_OPERATOR;

BOOL_OPERATOR: 'and' | 'or' | 'xor';

constant: INTEGER | DOUBLE | STRING | BOOL | NULL;

INTEGER: [0-9]+;
DOUBLE: [0-9]+ '.' [0-9]+;
STRING: ('"' ~'"'* '"') | ('\'' ~'\''* '\'');
BOOL: 'true' | 'false';
NULL: 'null';

block: '{' line* '}';

scope: '[' line* ']';

COMMENT
    : '#' ~[+\-\r\n] ~[\r\n]* // a '*' must be followed by something other than '+', '-' or a line break
    | '#' ( [\r\n]+ | EOF );  // a '*' is a valid comment if directly followed by a line break, or the EOF ;

WS: [ \t\r\n]+ -> skip;
IDENTIFIER: '@'? [a-zA-Z_][a-zA-Z0-9_]*;


