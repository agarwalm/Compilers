import compiler
from compiler.ast import *
import sys
import operator


filePath = sys.argv[1]

ast = compiler.parseFile(filePath)

#
#print ast

#make a dictionary of variables
varD = {}

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
		return n.value
	
	elif isinstance(n, Printnl):
		value = interpret(n.nodes[0])
		if not isinstance(value, int) or len(n.nodes)>1:
			raise Exception('ERROR! print can have only one constant integer argument.')
		
		else:
			print value
	
	elif isinstance(n, Name):
		if n.name not in varD:
			print "no assignment to "+n.name
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


	elif isinstance(n, Bitor):
		for i in range(0, len(n.nodes)):
			if not isinstance(interpret(n.nodes[i]), int):
				raise Exception('Error! Bitor can only be of interger values')
		
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
		for i in range(0, len(n.nodes)):
			if not isinstance(interpret(n.nodes[i]), int):
				raise Exception('Error! Bitxor can only be of integer values')
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

	elif isinstance(n.Mod):
		return interpret(n.left)%interpret(n.right)

	elif isinstance(n.Power):
		return interpret(n.left)**interpret(n.right)

	elif isinstance(n.FloorDiv):
		return interpret(n.left)//interpret(n.right)



		
								
								
								
	else:
		raise Exception('Error: unrecognized AST node')	






interpret(ast)
#THIS IS JUST FOR DEBUGGING PURPOSES
#TODO: delete it after we are done because the program should not print
# anything unless print is called in the other file
print varD
		

