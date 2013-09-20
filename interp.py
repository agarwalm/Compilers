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
			print "NODE:"
			print node
			return interpret(node)

	elif isinstance(n, Discard):
		return interpret(n.expr)

	elif isinstance(n, Assign):
		if not isinstance(n.nodes[0], AssName) or len(n.nodes)>1:
			print "ERROR! assign to only one variable please"
			return
		print n.nodes[0].name
		varD[n.nodes[0].name] = interpret(n.expr)

	elif isinstance(n, Add):
		return interpret(n.left) + interpret(n.right)

	elif isinstance(n, Sub):
		return interpret(n.left) - interpret(n.right)

	elif isinstance(n, Const):
		return n.value
	


interpret(ast)
print varD

		

