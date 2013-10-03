#Homework 2 Compiler
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola

import compiler
from compiler.ast import *
import sys
import operator


#from llvm import *
#from llvm.core import *

#the file to interpret is the first argument given 
filePath = sys.argv[1]

#abstract syntax tree for the contents of the file
ast = compiler.parseFile(filePath)
print ast
#print ast
#print ast
#dict to keep track of the mapping of variable names to stack slots
varToStack = {}

#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 0
vaD={}
flatStmts = [];


#takes a non flattened ast and returns a flattened ast
def flatten(n):
	
	if isinstance(n, Module):
		flatten(n.node)
	#iterate through all of the statement nodes 
	elif isinstance(n, Stmt):
		for x in n.nodes:
			flattenStmt(x)
	
	else:
		raise Exception('unrecognized AST')

def flattenStmt(n):
	#if you have an Assign, then use the given variable to assign
	#to the expression
	if isinstance(n, Assign):
		if isinstance(n.expr, Name):
			temp = Assign([AssName(genSymFromVar(n.nodes[0].name),'OP_ASSIGN')],flattenExp(n.expr,None))
			flatStmts.append(temp)
			
		else:
			flattenExp(n.expr, genSymFromVar(n.nodes[0].name))
		
	#if you have a discard, then generate a variable to assign
	#to the expression
	elif isinstance(n, Discard):
		flattenExp(n.expr, genSym())
		
	elif isinstance(n, Printnl):
		if (len(n.nodes) != 1):
			sys.exit('Miss an element to print.')
		a = genSym()
		b = genSym()
		t1 = flattenExp(n.nodes[0], a)
		n.nodes[0] =Name(t1)
		temp = Assign([AssName(b, 'OP_ASSIGN')], n)
		flatStmts.append(temp)
		return b
	
	elif isinstance(n, AugAssign):
		a = genSym()
		flattened_expr = flattenExp(n.expr, a)
		t1 = Name(flattened_expr)
		n.expr = t1
		temp = Assign([AssName(n.node, 'OP_ASSIGN')],n)
		flatStmts.append(temp)
		
	
	
	else:
		raise Exception('unrecognized AST')
		


def flattenExp(n, x):
	#assign a constant to the given variable and append to list
	if isinstance(n,Const):
		temp = Assign([AssName(x, 'OP_ASSIGN')],n)
		flatStmts.append(temp)
		return x
	#if we have a name, return a variable of the form %v
	if isinstance(n,Name):
		return genSymFromVar(n.name)
	

	if isinstance(n,Add) or isinstance(n,Div) or isinstance(n,Sub) or isinstance(n,Mul) or isinstance(n, LeftShift) or isinstance(n, RightShift) or isinstance(n, Power) or isinstance(n, Mod) or isinstance(n, FloorDiv):
		#generate symbols a and b 
		a = genSym()
		b = genSym()
		#use them to assign to constants (or if Names are the operands, will just return variable)
		leftStmt = flattenExp(n.left, a )
		rightStmt = flattenExp(n.right, b)
		#now we use the same operator object n and just change its left and right values
		n.left = Name(leftStmt)
		n.right = Name(rightStmt)
		#assign the add operation n to the varialbe x and append to the statements list
		temp = Assign([AssName(x, 'OP_ASSIGN')],n)
		flatStmts.append(temp)
		return x

	if isinstance(n,UnarySub) or isinstance(n, UnaryAdd):
		#tempExpr will take the value of the name assigned to it
		tempExpr = flattenExp(n.expr, x)
		#change the expression of the unary sub to the variable you assigned
		#to its expression when you flattened it
		n.expr = tempExpr
		#now assign the modified UnarySub, n, to variable x
		#and append it to the list
		temp = Assign([AssName(x, 'OP_ASSIGN')],n)
		flatStmts.append(temp)
		return x

	if isinstance(n, Bitand) or isinstance(n,Bitor) or isinstance(n, Bitxor):
		var = dict()
		lst = []
		#generate symbols and assign them to the first two
		#nodes of the bit operator
		a = genSym()
		b = genSym()
		flattened_exp1 = flattenExp(n.nodes[0], a)
		flattened_exp2 = flattenExp(n.nodes[1], b)
		
		#create the propper operation for the assignment
		if isinstance(n, Bitand):
			op = Bitand([Name(flattened_exp1),Name(flattened_exp2)])
		elif isinstance(n, Bitor):
			op = Bitor([Name(flattened_exp1),Name(flattened_exp2)])
		elif isinstance(n, Bitxor):
			op = Bitxor([Name(flattened_exp1),Name(flattened_exp2)])
		
		#make the assignment to the bit operator needed and add it to the
		#flatStmts list
		temp = Assign([AssName(x, 'OP_ASSIGN')],op)
		flatStmts.append(temp)
		
		#if you only have 2 operands,
		#add the assignment to the flatStmts list
		#note: the constant assignments were already made when you
		#called flattenExp on n.nodes[0] and n.nodes[1]
		if len(n.nodes)==2:
			return x
		
		#if you have more than two operands to bitAnd
		#you have to iterate through the list of nodes
		else:
			#the last variable that you assigned a bitAnd to
			currentVar = x
			
			for i in range(2, len(n.nodes)):
				c = genSym()
				d = genSym()
				
				flattenExpTemp = flattenExp(n.nodes[i], d)
				if isinstance(n, Bitand):
					opTemp = Bitand([Name(currentVar), Name(flattenExpTemp)])
				elif isinstance(n, Bitor):
					opTemp = Bitor([Name(currentVar), Name(flattenExpTemp)])
				elif isinstance(n, Bitxor):
					opTemp = Bitxor([Name(currentVar), Name(flattenExpTemp)])
				
				temp = Assign([AssName(c, 'OP_ASSIGN')], opTemp)
				flatStmts.append(temp)
				
				currentVar = c
			#this return value isn't actually needed
			#but just for the sake of consistency it is being returned
			return currentVar
	
	elif isinstance(n, Invert):
		a = genSym()
		flattened_expr = flattenExp(n.expr, a)
		t1 = Name(flattened_expr)
		n.expr = t1
		temp = Assign([AssName(n.expr, 'OP_ASSIGN')],n)
		flatStmts.append(temp)

		
				
	elif isinstance(n, CallFunc):
		lst = []
		for i in range(0, len(n.args)):
			a = genSym()
			flattened_expr = flattenExp(n.args[i], a)
			lst.append(Name(flattened_expr))
		n.args = lst
		temp = Assign([AssName(x, 'OP_ASSIGN')], n)
		flatStmts.append(temp)
		return x
	
	
	
	
	else:
		raise Exception('unrecognized AST')
		
			
			
			
			
		


	






#generates a unique variable name
def genSym():
	global varName
	name= '%'+ str(varName)
	varName += 1
	return name

#adds a % infront of a given variable name to generate
#an llvm-friendly variable
def genSymFromVar(v):
	vStr = "%"+v
	return vStr

	




print flatten(ast)
print flatStmts






		

