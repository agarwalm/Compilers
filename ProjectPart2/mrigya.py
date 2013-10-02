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
#print ast
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
		stmt=[]
		for x in n.nodes:
			y=flattenStmt(x)
			stmt.append(y)
			print y
		return Stmt(stmt)

def flattenStmt(n):
	if isinstance(n, Assign):
		return flattenExp(n.expr, n.nodes[0])


	elif isinstance(n, Discard):
		return flattenExp(n.expr, genSym() )



def flattenExp(n, x):
	#Add instance
	a='%N'
	b='%N'
	if isinstance(n, Add):
		op=Add(a,b)
		return binOp(n,x,op)
	elif isinstance(n,Sub):
		op=Sub(a,b)
		return binOp(n,x,op)
	elif isinstance(n,Mul):
		op=Mul(a,b)
		return binOp(n,x,op)
	elif isinstance(n,Div):
		op=Div(a,b)
		return binOp(n,x,op)
	elif isinstance(n,LeftShift):
		op=LeftShift(a,b)
		return binOp(n,x,op)
	elif isinstance(n,RightShift):
		op=RightShift(a,b)
		return binOp(n,x,op)
	elif isinstance(n,UnarySub):
		a=genSym()
		flattened = flattenExp(n.expr,a)
		flattened.append(ast.UnarySub(ast.Name(a)))
		return flattened
	

	elif isinstance(n, Bitand):
		var = dict()
		lst = []
		a = genSym()
		b = genSym()
		flattened_exp1 = flattenExp(n.nodes[0], a)
		flattened_exp2 = flattenExp(n.nodes[1], b)
		op = Bitand([a,b])
		
		op.nodes[0] = Name(a)
		op.nodes[1] = Name(b)
		
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		
		if (len(n.nodes)==2):

			return [flattened_exp1, flattened_exp2, Assign(x, op) ]
		
		
		lst.append(flattened_exp1)
		lst.append(flattened_exp2)
		lst.append(Assign(x, op))
			
		currentVar = x
		
			
		for i in range(2, len(n.nodes)):
			c = genSym()
			d = genSym()
			flattenExpTemp = flattenExp(n.nodes[i], d)
			lst.append(flattenExpTemp)
			opTemp = Bitand([currentVar, d])
			
			if (not isinstance(c,AssName)):
				c=[AssName(c,'OP_ASSIGN')]
				
			lst.append(Assign(c, opTemp))
			currentVar = c
		
		return lst
		
	
	elif isinstance(n, Bitor):
		var = dict()
		lst = []
		a = genSym()
		b = genSym()
		flattened_exp1 = flattenExp(n.nodes[0], a)
		flattened_exp2 = flattenExp(n.nodes[1], b)
		op = Bitor([a,b])
		
		op.nodes[0] = Name(a)
		op.nodes[1] = Name(b)
		
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		
		if (len(n.nodes)==2):

			return [flattened_exp1, flattened_exp2, Assign(x, op) ]
		
		
		lst.append(flattened_exp1)
		lst.append(flattened_exp2)
		lst.append(Assign(x, op))
			
		currentVar = x
		
			
		for i in range(2, len(n.nodes)):
			c = genSym()
			d = genSym()
			flattenExpTemp = flattenExp(n.nodes[i], d)
			lst.append(flattenExpTemp)
			opTemp = Bitor([currentVar, d])
			
			if (not isinstance(c,AssName)):
				c=[AssName(c,'OP_ASSIGN')]
				
			lst.append(Assign(c, opTemp))
			currentVar = c
		
		return lst
	
	elif isinstance(n, Bitxor):
		var = dict()
		lst = []
		a = genSym()
		b = genSym()
		flattened_exp1 = flattenExp(n.nodes[0], a)
		flattened_exp2 = flattenExp(n.nodes[1], b)
		op = Bitxor([a,b])
		
		op.nodes[0] = Name(a)
		op.nodes[1] = Name(b)
		
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		
		if (len(n.nodes)==2):

			return [flattened_exp1, flattened_exp2, Assign(x, op) ]
		
		
		lst.append(flattened_exp1)
		lst.append(flattened_exp2)
		lst.append(Assign(x, op))
			
		currentVar = x
		
			
		for i in range(2, len(n.nodes)):
			c = genSym()
			d = genSym()
			flattenExpTemp = flattenExp(n.nodes[i], d)
			lst.append(flattenExpTemp)
			opTemp = Bitxor([currentVar, d])
			
			if (not isinstance(c,AssName)):
				c=[AssName(c,'OP_ASSIGN')]
				
			lst.append(Assign(c, opTemp))
			currentVar = c
		
		return lst


	elif isinstance(n, Const):

		return [Assign(AssName(x, 'OP_ASSIGN'),n)]

	elif isinstance(n,Name):
		return Name(n.name)
	elif isinstance(n,AssName):
		print "hello"
		return




def binOp(n,x,op):
	if ((isinstance(n.left,Const))and (isinstance(n.right,Const))):
		a=genSym()
		b=genSym()
		l=flattenExp(n.left, a)
		r=flattenExp(n.right, b)
		op.left=Name(a)
		op.right=Name(b)
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		return [l,r,Assign(x,op)]

	elif(isinstance(n.left,Name)):
		a=genSym()
		r=flattenExp(n.right, a)
		op.left=n.left
		op.right=Name(a)
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		return [r, Assign(x,op)]
		
	elif(isinstance(n.right,Name)):
		a=genSym()
		l=flattenExp(n.left, a)
		op.left=Name(a)
		op.right=n.right
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		return [ l,Assign(x,op)]
	elif(isinstance(n.left,Name)and(isinstance(n.right,Name))):
		op.left=n.left
		op.right=n.right
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		return [Assign(x,op)]
	else:
		a=genSym()
		b=genSym()
		l=flattenExp(n.left,a)
		r=flattenExp(n.right,b)
		op.left=Name(a)
		op.right=Name(b)
		if (not isinstance(x,AssName)):
			x=[AssName(x,'OP_ASSIGN')]
		return [l,r,Assign(x,op)]



		
def genSym():
	global varName
	name= '%'+ str(varName)
	varName += 1
	return name
	

	




flatten(ast)


#TODO: after we have the flattened AST, we need to traverse it and generate LLVM code for each variable 





		

