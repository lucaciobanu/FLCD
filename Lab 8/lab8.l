
%{
	#include<stdio.h>
	
	int lineNumber =1;
	int correct =1;
	int badLine =0;
%}

%option noyywrap


LETTER [a-zA-Z]
DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
INTEGER [+-]?{NON_ZERO_DIGIT}{DIGIT}*
CHAR \'{LETTER}\'
STRING \"{CHAR}*\"
CONSTANT {INTEGER}|{CHAR}|{STRING}
IDENTIFIER  {LETTER}|{LETTER}({LETTER}|{DIGIT}|_)*?


%%
"Function" {printf("%s - as reserved word\n",yytext);}
"Main" {printf("%s - as reserved word\n",yytext);}
"Number" {printf("%s - as reserved word\n",yytext);}
"Vector" {printf("%s - as reserved word\n",yytext);}
"String" {printf("%s - as reserved word\n",yytext);}
"Character" {printf("%s - as reserved word\n",yytext);}
"read" {printf("%s - as reserved word\n",yytext);}
"show" {printf("%s - as reserved word\n",yytext);}
"verify" {printf("%s - as reserved word\n",yytext);}
"otherwise" {printf("%s - as reserved word\n",yytext);}
"forevery" {printf("%s - as reserved word\n",yytext);}
"aslongas" {printf("%s - as reserved word\n",yytext);}
"finish" {printf("%s - as reserved word\n",yytext);}
"increment" {printf("%s - as reserved word\n",yytext);}


{IDENTIFIER} printf( "- identifier: %s\n", yytext);
{CONSTANT} printf( "- constant: %s\n", yytext);

"{" {printf("%s - as separator\n", yytext);}
"}" {printf("%s - as separator\n", yytext);}
";" {printf("%s - as separator\n", yytext);}
"[" {printf("%s - as separator\n", yytext);}
"]" {printf("%s - as separator\n", yytext);}
"(" {printf("%s - as separator\n", yytext);}
")" {printf("%s - as separator\n", yytext);}
"," {printf("%s - as separator\n", yytext);}

"+" {printf("%s - as operator\n", yytext);}
"-" {printf("%s - as operator\n", yytext);}
"*" {printf("%s - as operator\n", yytext);}
"/" {printf("%s - as operator\n", yytext);}
"%" {printf("%s - as operator\n", yytext);}
"=" {printf("%s - as operator\n", yytext);}
"==" {printf("%s - as operator\n", yytext);}
"!=" {printf("%s - as operator\n", yytext);}
"<=" {printf("%s - as operator\n", yytext);}
">=" {printf("%s - as operator\n", yytext);}
"<" {printf("%s - as operator\n", yytext);}
">" {printf("%s - as operator\n", yytext);}
"&&" {printf("%s - as operator\n", yytext);}
"||" {printf("%s - as operator\n", yytext);}

[ \t]+ {}

[\n]+  {++lineNumber;}

. {correct = 0; badLine = lineNumber; printf("Incorrect:%s\n", yytext);}
 
%%
void main(int argc, char** argv)

{           
if (argc > 1)
{
    FILE *file;
    file = fopen(argv[1], "r");
    if (!file)
    {
        fprintf(stderr, "Could not open %s\n", argv[1]);
        exit(1);
    }
    yyin = file;
}

yylex();
if(correct == 1)
    printf("Correct program!");
else 
    printf("Incorrect program at line %d!", badLine);   
}
