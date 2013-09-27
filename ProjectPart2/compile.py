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

#dict to keep track of the mapping of variable names to stack slots
varToStack = {}

#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 0


#takes a non flattened ast and returns a flattened ast
def flatten(n):

	if isinstance(n, Module):
		#print n
		return Module(None, flatten(n.node))

	elif isinstance(n, Stmt):
		print n.nodes
		for x in n.nodes:
			print x
			print flattenStmt(x)
			return flattenStmt(x)

def flattenStmt(n):
	if isinstance(n, Assign):
		return flattenExp(n.exp, n.node)

	elif isinstance(n, Discard):
		print "here"
		return flattenExp(n.expr, genSym() )



def flattenExp(n, x):
	if isinstance(n, Add):
		a = genSym()
		b = genSym()
		return [ flattenExp(n.left, a), flattenExp(n.right, b), Assign(x, Add(a,b))]

	elif isinstance(n, Const):
		return [Assign(AssName(x, None), n)]





		
def genSym():
	global varName
	name= "%"+ str(varName)
	varName += 1
	return name
	

	




flatten(ast)


#TODO: after we have the flattened AST, we need to traverse it and generate LLVM code for each variable 





		

