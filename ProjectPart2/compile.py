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
#dict to keep track of the mapping of variable names to stack slots
varToStack = {}

#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 0
vaD={}


#takes a non flattened ast and returns a flattened ast
def flatten(n):

	if isinstance(n, Module):
		#print n
		return Module(None, flatten(n.node))

	elif isinstance(n, Stmt):
		for x in n.nodes:
			y=flattenStmt(x)
			print y
			return y

def flattenStmt(n):
	if isinstance(n, Assign):
		return flattenExp(n.expr, n.nodes[0])

	elif isinstance(n, Discard):
		return flattenExp(n.expr, genSym() )



def flattenExp(n, x):
	if isinstance(n, Add):

		a= genSym()
		b = genSym()
		l=flattenExp(n.left, a)
		r=flattenExp(n.right, b)
		add=Add(a,b)
		add.left=Name(a)
		add.right=Name(b)

		return [ r, l, Assign(x,add)]

	elif isinstance(n, Const):

		return [Assign(AssName(x, 'OP_ASSIGN'),n)]








		
def genSym():
	global varName
	name= '%'+ str(varName)
	varName += 1
	return name
	

	




flatten(ast)


#TODO: after we have the flattened AST, we need to traverse it and generate LLVM code for each variable 





		

