#!/usr/bin/env python
#
# Python lexer template.

#Mrigya Agarwal, Christine Graff, Giuseppe Mendola
#Use python version 2

import sys
import AstClasses as node
import ply.yacc as yacc

__author__ = "Ilya Yanok, Nate Nystrom"
__version__ = "Version 1.0, 10 Oct 2013"

states = (
		  ('indent', 'exclusive'),
		  ('dedent', 'exclusive'),
		  ('comment', 'exclusive'),
		  ('main', 'exclusive')
		  )

tokens = [
		  'indent', 'dedent', 'identifier', 'newline', 'comment',
		  'oparen', 'cparen', 'obracket', 'cbracket', 'ocurly', 'ccurly',
		  'string', 'integer', 'print', 'plus', 'minus', 'times', 'lparen', 'rparen', 'xor','and', 'or', 'invert', 'lshift', 'rshift', 'power', 'modulo', 'usub', 'uadd', 'equals', 'incassign', 'decassign', 'floorassign', 'floordiv', 'div', 'lt', 'gt', 'isequal', 'isnotequal', 'lequal', 'gequal', 'divassign', 'mulassign', 'modassign', 'lshiftassign', 'rshiftassign', 'andassign', 'orassign','xorassign', 'powerassign', 'input', 'comma', 'if', 'else', 'while', 'elif', 'true', 'false', 'colon', 'not', 'strand', 'stror', 'lambda', 'def', 'return'
		  ]

t_indent_ignore = ''
t_dedent_ignore = ''

def t_indent_error(t):
	pass

def t_dedent_error(t):
	pass

def t_comment_error(t):
	pass

def t_error(t):
	print "Illegal character '%s'" % t.value[0]
	t.lexer.skip(1)


#in any function you can put an optional documentation string.
#the ply library handles this in some way.
def t_comment_skip(t):
	r'[^\n]+'
	pass

def t_ANY_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)
	if len(t.lexer.paren_stack) == 0:
		t.lexer.curr_indent = 0
		if t.lexer.lexstate != 'indent':
			t.lexer.begin('indent')
			return t

def t_main_softnewline(t):
	r'\\\n'
	t.lexer.lineno += 1

def t_indent_comment(t):
	r'\#'
	t.lexer.begin('comment')

def char_val(c):
	if c == ' ':
		return 1
	elif c == '\t':
		return 8
	else:
		return 0

def t_indent_ws(t):
	r'[ \t]+'
	t.lexer.curr_indent += sum(map(char_val, t.value))

def process_indent(lexer):
	cnt = 0
	curr = lexer.curr_indent
	topi = lexer.indents.pop()
	while topi > curr:
		topi = lexer.indents.pop()
		cnt += 1
	lexer.indents.append(topi)
	if topi == curr:
		return -cnt
	if topi < curr:
		if cnt == 0:
			return 1
		print "Indentation error: unexpected indentation level ", curr
		return -cnt

def t_indent_indent(t):
	r'[^ \#\t\n]'
	t.lexer.lexpos -= 1
	val = process_indent(t.lexer)
	if val == 0:
		t.lexer.begin('main')
	elif val < 0:
		t.lexer.begin('dedent')
		t.lexer.dedent_cnt = -val
	else:
		t.lexer.indents.append(t.lexer.curr_indent)
		t.lexer.begin('main')
		return t

def t_dedent_dedent(t):
	r'.'
	t.lexer.lexpos -= 1
	t.lexer.dedent_cnt -= 1
	if t.lexer.dedent_cnt == 0:
		t.lexer.begin('main')
	return t

invert_paren = {
	'(' : ')',
	'[' : ']',
	'{' : '}'
}

paren_token_name = {
	'(' : 'oparen',
	')' : 'cparen',
	'[' : 'obracket',
	']' : 'cbracket',
	'{' : 'ocurly',
	'}' : 'ccurly'
}

reserved = {
	'print' : 'print',
}

def t_main_open(t):
	r'[\(\[\{]'
	t.lexer.paren_stack.append(invert_paren[t.value])
	t.type = paren_token_name[t.value]
	return t

def t_main_close(t):
	r'[\)\]\}]'
	last = t.lexer.paren_stack.pop()
	if last != t.value:
		print "Unmatched", t.value
		t.lexer.paren_stack.append(last)
	t.type = paren_token_name[t.value]
	return t

def token_override(self):
	t = self.token_()
	if t is None:
		return process_eof(self)
	return t

def process_eof(lexer):
	if len(lexer.indents) == 1:
		return None
	lexer.indents.pop()
	
	tok = lex.LexToken()
	tok.value = ''
	tok.type = 'dedent'
	tok.lineno = lexer.lineno
	tok.lexpos = lexer.lexpos
	tok.lexer = lexer
	return tok

###############

def process_string(string):
	# TODO: define me! (optional for P0, but need to do eventually)
	return string

def t_main_string_short_single(t):
	r"(r|R|UR|Ur|U|uR|ur|u|br|bR|b|BR|Br|B)?'[^'\n]*'"
	t.type = 'string'
	return process_string(t)

def t_main_string_short_double(t):
	r'(r|R|UR|Ur|U|uR|ur|u|br|bR|b|BR|Br|B)?"[^"\n]*"'
	t.type = 'string'
	return process_string(t)

literals = ".@,:`;~"

t_main_ignore = ' \t'


tokens += []

def t_main_lambda(t):
	r'lambda'
	return t

def t_main_def(t):
	r'def'
	return t

def t_main_return(t):
	r'return'
	return t

def t_main_input(t):
	r'input'
	return t


def t_main_while(t):
	r'while'
	return t

def t_main_if(t):
	r'if'
	return t

def t_main_else(t):
	r'else'
	return t

def t_main_elif(t):
	r'elif'
	return t

def t_main_isequal(t):
	r'\=\='
	return t

def t_main_gequal(t):
	r'>='
	return t

def t_main_lequal(t):
	r'<='
	return t

def t_main_isnotequal(t):
	r'!='
	return t

def t_main_floorassign(t):
	r'\/\/\='
	return t
	

def t_main_false(t):
	r'False'
	return t

def t_main_true(t):
	r'True'
	return t

def t_main_colon(t):
	r':'
	return t

def t_main_not(t):
	r'not'
	return t

def t_main_strand(t):
	r'and'
	return t

def t_main_stror(t):
	r'or'
	return t



def t_main_identifier(t):
	r'[a-zA-Z_][a-zA-Z_0-9]*'
	#check in the dictionary
	t.type = reserved.get(t.value, 'identifier');
	return t

def t_main_integer(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print "integer value too large", t.value
		t.value = 0
	return t

def t_main_incassign(t):
	r'\+\='
	return t

def t_comma(t):
	r'\,'
	return t

def t_main_decassign(t):
	r'\-\='
	return t

def t_main_powerassign(t):
	r'\*\*\='
	return t

def t_main_divassign(t):
	r'\/\='
	return t

def t_main_mulassign(t):
	r'\*\='
	return t

def t_main_modassign(t):
	r'\%\='
	return t

def t_main_lshiftassign(t):
	r'\<\<\='
	return t

def t_main_rshiftassign(t):
	r'\>\>\='
	return t

def t_main_andassign(t):
	r'\&\='
	return t

def t_main_orassign(t):
	r'\|\='
	return t

def t_main_xorassign(t):
	r'\^\='
	return t


def t_main_plus(t):
	r'\+'
	return t

def t_main_power(t):
	r'\*\*'
	return t

def t_main_minus(t):
	r'\-'
	return t

def t_main_times(t):
	r'\*'
	return t

def t_main_lparen(t):
	r'\('
	return t

def t_main_rparen(t):
	r'\)'
	return t

def t_main_and(t):
	r'\&'
	return t

def t_main_or(t):
	r'\|'
	return t

def t_main_xor(t):
	r'\^'
	return t

def t_main_invert(t):
	r'\~'
	return t

def t_main_lshift(t):
	r'\<\<'
	return t


def t_main_rshift(t):
	r'\>\>'
	return t



def t_main_modulo(t):
	r'\%'
	return t


def t_main_equals(t):
	r'\='
	return t

def t_main_floordiv(t):
	r'\/\/'
	return t

def t_main_div(t):
	r'\/'
	return t

def t_main_gt(t):
	r'>'
	return t

def t_main_lt(t):
	r'<'
	return t



def t_main_error(t):
	pass

def t_main_comment(t):
	'\#'
	t.lexer.begin('comment')


# Parser



precedence = (
			  ('nonassoc','print'),
			  ('nonassoc', 'if', 'elif', 'else', 'while'),
			  ('left', 'stror'),
			  ('left', 'strand'),
			  ('left','lt', 'gt','isequal', 'isnotequal', 'lequal', 'gequal', 'not' ),
			  ('left', 'or'),
			  ('left', 'xor'),
			  ('left', 'and'),
			  ('left', 'lshift', 'rshift'),
			  ('left','plus','minus'),
			  ('left', 'times', 'div', 'floordiv', 'modulo'),
			  ('right', 'uadd', 'usub', 'invert'),
			  ('right', 'power'),
			  )


def p_module(p):
	'module : stmt'
	p[0] = node.Module(p[1])


def p_stmt(p):
	'stmt : statement_list'
	p[0]=node.Stmt(p[1])

	
def p_single_statement_list(p):
	'statement_list : statement'
	p[0] = [p[1]]

def p_statement_list(p):
	'statement_list : statement_list statement'
	p[0] = p[1]+[p[2]]

def p_newline_statement(p):
	'statement : newline statement'
	p[0] = p[2]


def p_statement_newline(p):
	'statement : statement newline'
	p[0] = p[1]



def p_simple_statement(p):
	'statement : print expression'
	p[0] = node.Printnl([p[2]])

#def p_name_print(p):
#	'statement : print name'
#	p[0] = node.Printnl([p[2]])

#def p_input_exp(p):
#	'expression : input oparen parameters cparen'
#	p[0] = node.CallFunc(node.Name(p[1]),p[3])

def p_single_param(p):
	'parameters : expression'
	p[0] = [p[1]]

def p_params(p):
	'parameters : parameters comma expression '
	p[0] = p[1] + [p[1]]

def p_empty_params(p):
	'parameters : '
	p[0] = []

def p_assign_stmt(p):
	'statement : assname equals expression'
	p[0]= node.Assign(p[1], p[3])



def p_expression_statement(p):
	'statement : expression'
	p[0] = node.Discard(p[1])

def p_ifstmt(p):
	'statement : ifstmt'
	p[0] = p[1]

def p_whilestmt(p):
	'statement : whilestmt'
	p[0] = p[1]

def p_compoundState(p):
	'statement : compound_stmt'
	p[0] = p[1]

def p_simpst(p):
	'statement : simple_statement'
	p[0] = p[1]


def p_callingTheFunc(p):
	'expression : expression lparen parameters rparen'
	p[0] = CallFunc(p[1], p[3])

def p_lambdaThings(p):
	'expression : lambda id_list colon expression'
	p[0] = Lambda(p[2], p[4])

#how do you tell it epsilon?? Just a blank space?
def p_idList(p):
	'id_list : identifier'
	p[0] = [p[1]]
	

def p_idList2(p):
	'id_list : identifier comma id_list'
	p[0] = [p[1]]+p[3]

def p_returnStmt(p):
	'simple_statement : return expression'
	p[0] = p[2]


def p_compStmt(p):
	'compound_stmt : def identifier lparen id_list rparen colon suite'
	p[0] = Function(p[2], p[4], p[7])

def p_suite(p):
	'suite : newline indent statement_list dedent'
	p[0] = p[3]



def p_assign_ops(p):
	'''statement : name incassign expression
		| name decassign expression
		| name divassign expression
		| name mulassign expression
		| name modassign expression
		| name lshiftassign expression
		| name rshiftassign expression
		| name andassign expression
		| name orassign expression
		| name xorassign expression
		| name powerassign expression
		| name floorassign expression'''
	p[0] = node.AugAssign(p[1], p[2], p[3])




def p_bool(p):
	'expression : boolean'
	p[0] = p[1]

#def p_booleanexp(p):
#	'boolexp : boolean'
#	p[0] = p[1]


def p_unary_sub_expression(p):
	'expression : minus expression'
	p[0] = node.UnarySub(p[2])


def p_unary_add_expression(p):
	'expression : plus expression'
	p[0] = node.UnaryAdd(p[2])


def p_invert_expression(p):
	'expression : invert expression'
	p[0] = node.Invert(p[2])

#def p_boolexp(p):
#	'''boolexp : expression lt expression
#		| expression gt expression
#		| expression lequal expression
#		| expression gequal expression
#		| expression isnotequal expression
#		| expression isequal expression'''
#	p[0] = node.BoolExp(p[1], p[2], p[3], None)



def p_high_prec_expression(p):
	'expression : expression0'
	p[0] = p[1]

def p_bracket_expression(p):
	'expression : oparen expression cparen'
	p[0] = p[2]

def p_negation(p):
	'expression : not expression'
	p[0] = node.Not(p[2])

def p_name_exp(p):
	'expression : name'
	p[0] = p[1]


def p_binary_operators(p):
	'''expression : expression plus expression
		| expression minus expression
		| expression times expression
		| expression div expression
		| expression power expression
		| expression modulo expression
		| expression lshift expression
		| expression rshift expression
		| expression floordiv expression
		| expression and expression
		| expression or expression
		| expression xor expression
		| expression strand expression
		| expression stror expression
		| expression lt expression
		| expression gt expression
		| expression lequal expression
		| expression gequal expression
		| expression isnotequal expression
		| expression isequal expression'''
	
	if p[2] == '+':
		p[0] = node.Add(p[1], p[3])
	elif p[2] == '-':
		p[0] = node.Sub(p[1], p[3])
	elif p[2] == '*':
		p[0] = node.Mul(p[1], p[3])
	elif p[2] == '/':
		p[0] = node.Div(p[1], p[3])
	elif p[2] == '**':
		p[0] = node.Power(p[1], p[3])
	elif p[2] == '%':
		p[0] = node.Mod(p[1], p[3])
	elif p[2] == '//':
		p[0] = node.FloorDiv(p[1], p[3])
	elif p[2] == '>>':
		p[0] = node.RightShift(p[1], p[3])
	elif p[2] == '<<':
		p[0] = node.LeftShift(p[1], p[3])
	elif p[2] == '&':
		p[0] = node.Bitand(p[1],p[3])
	elif p[2] == '|':
		p[0] = node.Bitor(p[1],p[3])
	elif p[2] == '^':
		p[0] = node.Bitxor(p[1],p[3])
	elif p[2] == '==' or p[2] == '>' or p[2] == '<' or p[2] == '<=' or p[2] == '>=' or p[2] == '!=':
		p[0] = node.BoolExp(p[1], p[2], p[3], None)
	elif p[2] == 'and' or p[2] == 'or':
		p[0] = node.BoolExp(p[1], p[2], p[3], None)



	


def p_if(p):
	'ifstmt : if expression colon newline indent statement_list dedent'
	p[2].flag = "check"
	p[0] = node.IfNode(p[2],p[6],[], "")

def p_if_with_else(p):
	'ifstmt : if expression colon newline indent statement_list dedent elsestmt'
	p[2].flag = "check"
	p[0] = node.IfNode(p[2],p[6],p[8], "")

def p_else(p):
	'elsestmt : else colon newline indent statement_list dedent'
	p[0] = p[5]

def p_elif(p):
	'elsestmt : elif expression colon newline indent statement_list dedent'
	p[2].flag = "check"
	p[0] = node.IfNode(p[2], p[6], [], "")

def p_elif_with_else(p):
	'elsestmt : elif expression colon newline indent statement_list dedent elsestmt'
	p[2].flag = "check"
	p[0] = node.IfNode(p[2], p[6], p[8], "")

def p_while(p):
	'whilestmt : while expression colon newline indent statement_list dedent'
	p[2].flag = "check"
	p[0] = node.WhileNode(p[2], p[6])


#def p_exprList(p):
#	'expr_list : expression'
#	p[0] = [p[1]]
#
#def p_exprList2(p):
#	'expr_list : expression comma expr_list'
#	p[0] = [p[1]]+p[3]


		
def p_int_expression(t):
	'expression0 : num'
	t[0] = t[1]

def p_exp_name(t):
	'expression0 : name'
	t[0] = t[1]

def p_exp_bool(t):
	'expression0 : boolean'
	t[0] = t[1]

def p_const_rule(t):
	'num : integer'
	#include boxing here
	t[0] = node.Const(t[1])


def p_assname(t):
	'assname : identifier'
	t[0] = node.AssName(t[1])

def p_name(t):
	'name : identifier'
	t[0] = node.Name(t[1])


	

def p_boolean(t):
	'''boolean : true
		       | false'''
	if t[1] == "True":
		#boxing (true turns to 5 and false turns to 1 for some reason)
		t[0] = node.Bool(1, None)
	elif t[1] == "False":
		t[0] = node.Bool(0, None)

def p_error(t):
	sys.exit('Illegal P0 operation')



import ply.lex as lex


def getAST():
	lexer = lex.lex()
	lexer.indents = []
	lexer.indents.append(0)
	lexer.paren_stack = []
	lexer.curr_indent = 0
	lexer.token_ = lexer.token
	lexer.token = (lambda: token_override(lexer))
	lexer.begin('indent')
	yacc.yacc(debug=1)
	file = sys.argv[1]
	stream = open(file)
	contents = stream.read()
	lex.runmain(lexer)
	ast=yacc.parse(contents, lexer)
	return ast

getAST()








