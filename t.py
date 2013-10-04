#Homework 2 Compiler
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola

import compiler
from compiler.ast import *
import sys
import operator


#from llvm import *
#from llvm.core import *

#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 0
#the list of flattened statement nodes
flatStmts = [];

def compile():
	#the file to interpret is the first argument given
	filePath = sys.argv[1]
	
	#abstract syntax tree for the contents of the file
	ast = compiler.parseFile(filePath)
	#print "original ast: ", ast, "\n ********"
	#flatten the ast
	#(fill the flatStmts tree with assignment statements)
	flatten(ast)
	
	#output first line needed for the .ll file
	print "define i32 @main() nounwind uwtable ssp {"
	
	#print "statements list after flattening: ", flatStmts
	alloc()
	
	#TODO: before generating the llvm code from the statements,
	#iterate over the flatStmts list and generate
	#an alloca for each variable (so you don't have to worry about it later)
	
	#iterate through all of the statments generated by the
	#flattening (located in flatStmts list)
	#and generate LLVM code
	for s in flatStmts:
		astToLLVM(s, None)
	
	#output what you need for the end of the main function in the .ll file
	print "	 "+"ret i32 0"
	print "}"
		




#takes a non flattened ast and returns a flattened ast
def flatten(n):
	
	if isinstance(n, Module):
		flatten(n.node)
	#iterate through all of the statement nodes 
	elif isinstance(n, Stmt):
		for x in n.nodes:
			flattenStmt(x)

def flattenStmt(n):
	#if you have an Assign, then use the given variable to assign
	#to the expression
	if isinstance(n, Assign):
		if isinstance(n.expr, Name):
			temp = Assign([AssName(genSymFromVar(n.nodes[0].name),'OP_ASSIGN')],Name(flattenExp(n.expr,None)))
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
	

	if isinstance(n,Add) or isinstance(n,Div) or isinstance(n,Sub) or isinstance(n,Mul) or isinstance(n, LeftShift) or isinstance(n, RightShift) or isinstance(n,Power) or isinstance(n, Mod) or isinstance(n, FloorDiv):
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
		n.expr = Name(tempExpr)
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
	name= '%.'+ str(varName)
	varName += 1
	return name

#adds a % infront of a given variable name to generate
#an llvm-friendly variable
def genSymFromVar(v):
	vStr = "%."+v
	return vStr


#generates llvm code from an Assign statement
def astToLLVM(ast, x):
	
	
	if isinstance(ast, Assign):
		if isinstance(ast.expr, Const):
			print "	 "+ "store i32 "+str(ast.expr.value)+", i32* " + ast.nodes[0].name+", align 4"
		else:
			astToLLVM(ast.expr, ast.nodes[0].name)
	
	
	elif isinstance(ast, Const):
		o = constant(ast);
		return o.toString
	
	elif isinstance(ast, Add):
		return createOpObj(ast, x, "add")
	
	
	elif isinstance(ast, Sub):
		return createOpObj(ast,"sub")
	
	elif isinstance(ast, Mul):
		return createOpObj(ast, "mul")
	
	elif isinstance(ast, Div):
		return createOpObj(ast,"div")

	elif isinstance(ast, Power):
		return createOpObj(ast, "pow")

	elif isinstance(ast, Mod):
		return createOpObj(ast, "mod")

	elif isinstance(ast, LeftShift):
		return createOpObj(ast,"LeftShift")

	elif isinstance(ast, RightShift):
		return createOpObj(ast, "RightShift")
	
	elif isinstance(ast, AssName):
		return ast.name
	
	elif isinstance(ast, Name):
		return ast.name

	elif isinstance(ast, UnarySub):
		o = unarySub(ast)
		return o.toString

	elif isinstance(ast, load):
		return ast.toString
		
def alloc():

	lst = []
	for element in flatStmts:
		if element.nodes[0].name not in lst:
			lst.append(element.nodes[0].name)
	for element in lst:
		print "	 "+element + " = alloca i32, align 4"

		
	
	



#creates an llvmOp object for a specified operator (add, sub, mul, div or power)
def createOpObj(ast, x, op):
	l = astToLLVM(ast.left,x)
	r = astToLLVM(ast.right,x)
	varName = x
	obj = llvmOp(l, r, op, varName)
	return obj.codegen()


#class for operators (add, sub, mul, div or power)
class llvmOp:
	def __init__(self, l, r, op, x):
		self.left = l
		self.right = r
		self.operation = op
		self.assignTo = x

	def codegen(self):
		a = genSym()
		b = genSym()
		obj1 = load(self.left, a)
		obj2 = load(self.right, b)

		c = genSym()
		temp1 = Assign([AssName(a, 'OP_ASSIGN')], obj1)
		temp2 = Assign([AssName(b, 'OP_ASSIGN')], obj2)
		print astToLLVM(obj1, a)
		print astToLLVM(obj2, b)
		print "	 "+c+" = "+self.operation+" nsw i32 "+a+", "+b
		print "	 "+"store i32 "+c+", i32* "+self.assignTo+", align 4"
		return "hello"
	
		
#	def codegen2(self):
		
		

#class for constants
class constant:
	def __init__(self, c):
		self.val = c.value;
		self.toString = str(self.val)

class unarySub:
	def __init__(self, u):
		self.exp = str(astToLLVM(u.expr))
		self.toString = "However you express: -"+self.exp+" in llvm"

#class printClass:
#	def __init__(self,u):
#		self.
		
class load:
	def __init__(self, var,a):
		self.toString = "	 "+a+" = load i32* "+ var+", align 4"


	




compile()







		

