#Homework 1 P0 Interpreter
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola

import compiler
from compiler.ast import *
import sys
import operator

#the file to interpret is the first argument given 
filePath = sys.argv[1]

#abstract syntax tree for the contents of the file
ast = compiler.parseFile(filePath)

#make a dictionary of variables
varD = {}

#the function which interprets the module recursively
def interpret(n):
	
	if isinstance(n, Module):
		interpret(n.node)
	
	elif isinstance(n, Stmt):
		for node in n:
			interpret(node)
	
	elif isinstance(n, Discard):
		return interpret(n.expr)
	
	elif isinstance(n, Assign):
		if not isinstance(n.nodes[0], AssName) or len(n.nodes)>1:
			print "ERROR! assign to only one variable please"
			return
		val = interpret(n.expr)
		varD[n.nodes[0].name] = val
		return val
	
	elif isinstance(n, Add):
		return interpret(n.left) + interpret(n.right)
	
	elif isinstance(n, Sub):
		return interpret(n.left) - interpret(n.right)
	
	elif isinstance(n, Mul):
		return interpret(n.left) * interpret(n.right)
	
	elif isinstance(n,Div):
		return interpret(n.left)/interpret(n.right)
	
	
	elif isinstance(n, Invert):
		return -(interpret(n.expr)+1)
	
	elif isinstance(n, Const):
		if not isinstance(n.value, int):
			raise Exception( 'ERROR! All constants must be integer values')
		else:
			return n.value
	
	elif isinstance(n, Printnl):
		value = interpret(n.nodes[0])
		if len(n.nodes)>1:
			raise Exception('ERROR! print can have only one argument.')
		
		else:
			print value
	
	elif isinstance(n, Name):
		if n.name not in varD:
			raise Exception('ERROR! no assignment to '+n.name)
		return varD[n.name]
	
	elif isinstance(n, AssName):
		return interpret(n.name)
	
	elif isinstance(n, CallFunc):
		value = None
		if n.node.name == 'input':
			value = input("Enter an integer: ")
			while not isinstance(value, int):
				print "The value should be an integer"
				value = input("Enter an integer: ")
			return value	
		
			
		else:
			raise Exception('ERROR! Function not recognized')

	elif isinstance(n, Bitor):
		bitorVal = interpret(n.nodes[0])
		for i in range(1, len(n.nodes)):
			bitorVal =  bitorVal | interpret(n.nodes[i]) 
		return bitorVal
	
	elif isinstance(n, Bitand):
		bitAndVal = interpret(n.nodes[0])
		for i in range(1, len(n.nodes)):
			bitAndVal = bitAndVal & interpret(n.nodes[i])
		return bitAndVal
	
	elif isinstance(n, Bitxor):
		bitXorVal = interpret(n.nodes[0])
		for i in range(1, len(n.nodes)) :
			bitXorVal = bitXorVal ^ interpret(n.nodes[i])
		return bitXorVal

	elif isinstance(n,LeftShift):
		return interpret(n.left)<<interpret(n.right)

	elif isinstance(n,RightShift):
		return interpret(n.left)>>interpret(n.right)

	elif isinstance(n,UnarySub):
		return -interpret(n.expr)

	elif isinstance(n,UnaryAdd):
		return +interpret(n.expr)

	elif isinstance(n,AugAssign):
		ops = { "+=": operator.add, "-=": operator.sub 
		,"*=": operator.mul, "/=": operator.div
		, "<<=": operator.lshift,">>=": operator.rshift
		,"|=": operator.or_, "&=": operator.and_
		,"^=": operator.xor 
		,"**=": operator.pow 
		,"%=": operator.mod}
		varD[n.node.name]=ops[n.op](interpret(n.node),interpret(n.expr))
		return varD[n.node.name]

	elif isinstance(n,Mod):
		return interpret(n.left)%interpret(n.right)

	elif isinstance(n,Power):
		return interpret(n.left)**interpret(n.right)

	elif isinstance(n,FloorDiv):
		return interpret(n.left)//interpret(n.right)

	
	else:
		raise Exception('Error: unrecognized AST node')	


#run the interpret function on the abstract syntax tree
interpret(ast)

		

