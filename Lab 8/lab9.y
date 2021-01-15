%{
	#include<stdio.h>
	#include<stdlib.h>

	#define YYDEBUG 1
%}

%token IDENTIFIER
%token CONSTANT
%token FUNCTION
%token MAIN
%token NUMBER
%token STRING
%token CHARACTER
%token READ
%token SHOW
%token VECTOR 
%token VERIFY 
%token OTHERWISE
%token ASLONGAS
%token FOREVERY
%token FINISH
%token INCREMENT
%token SEMICOLON
%token COMMA
%token LEFT_CURLY_BRACKET
%token RIGHT_CURLY_BRACKET
%token LEFT_SQUARE_BRACKET
%token RIGHT_SQUARE_BRACKET
%token LEFT_ROUND_BRACKET
%token RIGHT_ROUND_BRACKET
%token OR
%token AND
%token MINUS
%token PLUS
%token SMALLER_OR_EQUAL
%token GREATER_OR_EQUAL
%token SMALLER
%token GREATER
%token EQUAL
%token ASSIGNMENT
%token DIFFERENT
%token DIV
%token MOD
%token MULTIPLY

%start program

%% 
program : FUNCTION MAIN LEFT_ROUND_BRACKET RIGHT_ROUND_BRACKET LEFT_CURLY_BRACKET declarationList stmtList RIGHT_CURLY_BRACKET ;
declarationList : declaration | declaration declarationList ;
identifierList : IDENTIFIER SEMICOLON | IDENTIFIER COMMA identifierList ;
declaration : type identifierList;
type : mainTypes | arraysDecl ;
mainTypes : NUMBER | CHARACTER | STRING | VECTOR ;
arraysDecl : mainTypes LEFT_SQUARE_BRACKET CONSTANT RIGHT_SQUARE_BRACKET ;

vectorItem : IDENTIFIER LEFT_SQUARE_BRACKET IDENTIFIER RIGHT_SQUARE_BRACKET | IDENTIFIER LEFT_SQUARE_BRACKET CONSTANT RIGHT_SQUARE_BRACKET ;
item : IDENTIFIER | CONSTANT | vectorItem ;
operator : PLUS | MINUS | MULTIPLY | DIV | MOD ;
expression : item operator expression | item operator item | item | LEFT_ROUND_BRACKET item operator expression RIGHT_ROUND_BRACKET | LEFT_ROUND_BRACKET item operator item RIGHT_ROUND_BRACKET ;

RELATION : SMALLER | SMALLER_OR_EQUAL | EQUAL | DIFFERENT | GREATER_OR_EQUAL | GREATER ;

stmtList : stmt | stmt stmtList ;
stmt : assignStmt| inStmt | outStmt | ifStmt | whileStmt | forStmt ;
assignStmt : IDENTIFIER ASSIGNMENT expression SEMICOLON | vectorItem ASSIGNMENT expression SEMICOLON;
inStmt : READ GREATER GREATER IDENTIFIER SEMICOLON | READ GREATER GREATER vectorItem SEMICOLON ;
outStmt : SHOW SMALLER SMALLER CONSTANT  SEMICOLON | SHOW SMALLER SMALLER  IDENTIFIER  SEMICOLON; 
ifStmt : VERIFY LEFT_ROUND_BRACKET condition RIGHT_ROUND_BRACKET LEFT_CURLY_BRACKET stmtList RIGHT_CURLY_BRACKET | VERIFY LEFT_ROUND_BRACKET condition RIGHT_ROUND_BRACKET LEFT_CURLY_BRACKET stmtList RIGHT_CURLY_BRACKET OTHERWISE LEFT_CURLY_BRACKET stmtList RIGHT_CURLY_BRACKET ;
whileStmt : ASLONGAS LEFT_ROUND_BRACKET condition RIGHT_ROUND_BRACKET LEFT_CURLY_BRACKET stmtList RIGHT_CURLY_BRACKET ;
forStmt : FOREVERY LEFT_ROUND_BRACKET IDENTIFIER COMMA expression COMMA expression COMMA CONSTANT RIGHT_ROUND_BRACKET LEFT_CURLY_BRACKET stmtList RIGHT_CURLY_BRACKET ;
condition : expression RELATION expression ;
%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if (argc > 1) 
    yyin = fopen(argv[1], "r");
  if ( (argc > 2) && ( !strcmp(argv[2], "-d") ) ) 
    yydebug = 1;
  if ( !yyparse() ) 
    fprintf(stderr,"\t Good !!!\n");
}
