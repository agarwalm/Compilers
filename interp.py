import compiler
from compiler.ast import *
import sys


filePath = sys.argv[1]

ast = compiler.parseFile(filePath)


print ast

#make a dictionary of variables
varD = {}

def interpret(n):
	
	if isinstance(n, Module):
		return interpret(n.node)
	
	elif isinstance(n, Stmt):
		for node in n:
			interpret(node)
	
	elif isinstance(n, Discard):
		return interpret(n.expr)
	
	elif isinstance(n, Assign):
		if not isinstance(n.nodes[0], AssName) or len(n.nodes)>1:
			print "ERROR! assign to only one variable please"
			return
		varD[n.nodes[0].name] = interpret(n.expr)
	
	
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
		return n.value
	
	elif isinstance(n, Printnl):
		value = interpret(n.nodes[0])
		if not isinstance(value, int) or len(n.nodes)>1:
			raise Exception('ERROR! print can have only one constant integer argument.')
		
		else:
			print interpret(n.nodes[0])
	
	elif isinstance(n, Name):
		if n.name not in varD:
			print "ERROR"
			return
		return varD[n.name]
	
	elif isinstance(n, AssName):
		return interpret(n.name)
	
	elif isinstance(n, CallFunc):
		value = None
		if n.node.name == 'input':
			value = input("Enter an integer: ")
		else:
			raise Exception('Function not recognized')
			return value
#		else:
#			raise Exception('Error: unrecognized AST node')

	elif isinstance(n, Bitor):
		bitorVal = interpret(n.nodes[0])
		for i in range(1, len(n.nodes)):
			bitorVal =  bitorVal | interpret(n.nodes[i]) 
		return bitorVal
								
		







interpret(ast)
print varD
		

