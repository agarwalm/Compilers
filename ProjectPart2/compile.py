#Homework 2 Compiler
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola
import sys
import operator
import os
import a3test
from AstClasses import *



#from llvm import *
#from llvm.core import *

#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 4
#the list of flattened statement nodes
flatStmts = [];

#gets creates an ast from the contenst of a file name given as an argument
#generates LLVM code from the contents of the file
def compile():
	#check that the user has given exactly one file as input
	assert(len(sys.argv) == 2);
	
	#the file to interpret is the first argument given
	filePath = sys.argv[1]
	#abstract syntax tree for the contents of the file
	ast=a3test.getAST()
	#ast = compiler.parseFile(filePath)
	#print "original ast: ", ast, "\n ********"
	#flatten the ast
	#(fill the flatStmts tree with assignment statements)
	
	flatten(ast)
	# print "///////////////////////////////////////"
	# print ast
	# print "///////////////////////////////////////"
	print '@.str = private unnamed_addr constant [3 x i8] c"%d\\00", align 1'
	print '@.str1 = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1'
	print 'define i32 @input() nounwind uwtable ssp {'
	print '  %n = alloca i32, align 4'
	print '  %1 = call i32 (i8*, ...)* @scanf(i8* getelementptr inbounds ([3 x i8]* @.str, i32 0, i32 0), i32* %n)'
	print '  %2 = load i32* %n, align 4'
	print '  ret i32 %2'
	print '}\n'
	print 'declare i32 @scanf(i8*, ...)\n'
	print 'define i32 @print_int_nl(i32 %x) nounwind uwtable ssp {'
	print '  %1 = alloca i32, align 4'
	print '  store i32 %x, i32* %1, align 4'
	print '  %2 = load i32* %1, align 4'
	print '  %3 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str1, i32 0, i32 0), i32 %2)'
	print '  ret i32 0'
	print '}\n'
	print 'declare i32 @printf(i8*, ...)'
	
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
	print "declare double @floor(double) nounwind readnone"
	print "declare double @llvm.pow.f64(double, double) nounwind readonly"
		
		




#takes a non flattened ast and returns a flattened ast
def flatten(n):
	
	if isinstance(n, Module):
		flatten(n.nodes)
	#iterate through all of the statement nodes 
	elif isinstance(n, Stmt):
		for x in n.nodes:
			flattenStmt(x)

def flattenStmt(n):
	#if you have an Assign, then use the given variable to assign
	#to the expression
	if isinstance(n, Assign):
		if not isinstance(n.name, AssName): #or len(n.nodes)>1:
			sys.exit('Tuple assignment not permitted')

		if isinstance(n.expr, Name):

			temp = Assign(AssName(genSymFromVar(n.name.name)),Name(flattenExp(n.expr,genSym())))
			flatStmts.append(temp)
			
		else:
			flattenExp(n.expr, genSymFromVar(n.name.name))
		
	#if you have a discard, then generate a variable to assign
	#to the expression
	elif isinstance(n, Discard):
		flattenExp(n.expr, genSym())

	elif isinstance(n, Printnl):
		if (len(n.nodes) != 1):
			sys.exit('Print accepts a single integer value')
		a = genSym()
		b = genSym()
		t1 = flattenExp(n.nodes[0], a)
		n.nodes[0] =Name(t1)
		temp = Assign(AssName(b), n)
		flatStmts.append(temp)
		return b
	
	elif isinstance(n, AugAssign):
		a = genSym()
		flattened_expr = flattenExp(n.expr, a)
		t1 = Name(flattened_expr)
		n.expr = t1
		n.node = Name(genSymFromVar(n.node.name))
		temp = Assign(AssName(n.node.name),n)
		flatStmts.append(temp)



	else:
		sys.exit('unrecognized AST')



def flattenExp(n, x):
	#assign a constant to the given variable and append to list
	if isinstance(n,Const):
		if not isinstance(n.value, int):
			sys.exit('ERROR! All constants must be integer values')
		temp = Assign(AssName(x),n)
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
		temp = Assign(AssName(x),n)
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
		temp = Assign(AssName(x),n)
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
		temp = Assign(AssName(x),op)
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
				
				temp = Assign(AssName(c), opTemp)
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
		temp = Assign(AssName(n.expr),n)
		flatStmts.append(temp)



	elif isinstance(n, CallFunc):
		lst = []
		for i in range(0, len(n.args)):
			a = genSym()
			flattened_expr = flattenExp(n.args[i], a)
			lst.append(Name(flattened_expr))
		n.args = lst
		temp = Assign(AssName(x), n)
		flatStmts.append(temp)
		return x
		
	
	else:
		sys.exit('unrecognized AST')

		
				
			
			
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

#prints all alloca instructions for the variables in the flatStmts list
def alloc():
	
	lst = []
	for element in flatStmts:
		if element.name.name not in lst:
			lst.append(element.name.name)
	
	for element in lst:
		print "	 "+element + " = alloca i32, align 4"


#generates llvm code from the Assign statements in the flatStmts list
def astToLLVM(ast, x):
	
	
	if isinstance(ast, Assign):
		#if the assign statement has only one constant to the right of the equals sign, output a store instruction
		if isinstance(ast.expr, Const):
			print "	 "+ "store i32 "+str(ast.expr.value)+", i32* " + ast.name.name+", align 4"
		if isinstance(ast.expr, Name):
			a = genSym()
			obj = load(ast.expr.name, a)
			print astToLLVM(obj, a)
			print "  "+"store i32 "+a+", i32* " + ast.name.name+", align 4"
		#otherwise it means there is a more complex expression to the right of the equals sign
		#we need to go deeper
		else:
			astToLLVM(ast.expr, ast.name.name)
	
	elif isinstance(ast, Const):
		o = constant(ast);
		return o.toString
	
	elif isinstance(ast, Add):
		return createOpObj(ast, x, "add")
	
	elif isinstance(ast, Sub):
		return createOpObj(ast,x,"sub")
	
	elif isinstance(ast, Mul):
		return createOpObj(ast,x, "mul")
	
	elif isinstance(ast, Div):
		return createOpObj(ast,x,"sdiv")


	elif isinstance(ast, Mod):
		return createOpObj(ast,x, "srem")

	elif isinstance(ast, LeftShift):
		return createOpObj(ast,x,"shl")

	elif isinstance(ast, RightShift):
		return createOpObj(ast,x, "ashr")

	elif isinstance(ast, FloorDiv):
		return createFloorObj(ast,x)
	
	elif isinstance(ast, Power):
		return createPowObj(ast,x)
	

	elif isinstance(ast, Bitor):
		return createBitOpObj(ast,x, "or")

	elif isinstance(ast, Bitand):
		return createBitOpObj(ast,x, "and")

	elif isinstance(ast, Bitxor):
		return createBitOpObj(ast,x, "xor")
	
	elif isinstance(ast, AssName):
		return ast.name
	
	elif isinstance(ast, Name):
		return ast.name

	elif isinstance(ast, UnarySub):
		return createUnaryOpObj(ast,x,"us")

	elif isinstance(ast, UnarySub):
		return createUnaryOpObj(ast,x,"ua")

	elif isinstance(ast, AugAssign):
		return createAugObj(ast,ast.node.name,ast.op)

	elif isinstance(ast, Printnl):
		return createPrintObj(ast, x)

	elif isinstance(ast, CallFunc):
		return createCallFuncObj(ast, x)
	
	
	elif isinstance(ast, load):
		return ast.toString

		
	
#creates an llvmOp object for a specified operator (add, sub, mul, div or power)
#returns the generated code
def createOpObj(ast, x, op):
	#get the value of .left and .right (will either be a variable or a constant)
	l = astToLLVM(ast.left,x)
	r = astToLLVM(ast.right,x)
	#creates the an llvmOp object with the propper operation
	obj = llvmOp(l, r, op, x)
	return obj.codegen()

#creates an llvmOp object for a specified bitwise operator (and, or, xor)
#the bit operators do not have a .left and .right, but because we flattened the
#ast, each bitwise operator will only have two nodes .nodes[0] and .nodes[1]
def createBitOpObj(ast,x,op):
	l = astToLLVM(ast.nodes[0],x)
	r = astToLLVM(ast.nodes[1],x)
	obj = llvmOp(l, r, op, x)
	return obj.codegen()

#for UnarySub, just subtract the expression from 0
def createUnaryOpObj(ast, x,op):
	e = astToLLVM(ast.expr,x)
	if(op == "us"):
		obj = UnaryllvmOp(e,"sub",x)
	else:
		obj = UnaryllvmOp(e,"add",x)

	return obj.codegen()

def createPrintObj(ast, x):
	e = astToLLVM(ast.nodes[0], genSym())
	obj = Printllvm(e,x)
	return obj.codegen()

def createCallFuncObj(ast,x):
	a = genSym()
	print "	 "+a+" = call i32 @"+ast.node.name+"()"
	print "	 "+"store i32 "+a+", i32* "+x+", align 4"

def createFloorObj(ast,x):
	l = astToLLVM(ast.left, x)
	r = astToLLVM(ast.right,x)
	obj = FloorllvmOp(l,r, x)
	return obj.codegen()
	
def createPowObj(ast,x):
	l = astToLLVM(ast.left, x)
	r = astToLLVM(ast.right,x)
	obj = PowllvmOp(l,r,x)
	obj.codegen()	
	
	
	

def createAugObj(ast, x, op):
	e = astToLLVM(ast.expr, x)
	if(op == "+="):
		obj = AugllvmOp(e, "add", x)
	elif(op == "-="):
		obj = AugllvmOp(e,"sub",x)
	elif(op == "/="):
		obj = AugllvmOp(e,"sdiv", x)
	elif(op == "*="):	
		obj = AugllvmOp(e,"mul", x)
	elif(op == "%="):
		obj = AugllvmOp(e,"srem", x)
	elif (op == "<<="):
		obj = AugllvmOp(e,"shl",x)
	elif (op == ">>="):
		obj = AugllvmOp(e,"ashr",x)
	elif (op == "&="):
		obj = AugllvmOp(e, "and", x)
	elif (op == "|="):
		obj = AugllvmOp(e,"or",x)
	elif (op == "^="):
		obj = AugllvmOp(e,"xor",x)
	elif (op == "**="):
		obj = AugllvmOp(e,"pow",x)

	return obj.codegen()


#class for operators (add, sub, mul, div or power)
class llvmOp:
	def __init__(self, l, r, op, x):
		self.left = l
		self.right = r
		self.operation = op
		self.assignTo = x
	#generates certain lines of llvm code that needs to be printed for a given operation
	def codegen(self):
		#must create temporary variables for the load operations
		a = genSym()
		b = genSym()
		obj1 = load(self.left, a)
		obj2 = load(self.right, b)
		#temporary variable to store the operation before it can be stored in x
		c = genSym()
		#create assignments for the temporary variables
#		temp1 = Assign([AssName(a, 'OP_ASSIGN')], obj1)
#		temp2 = Assign([AssName(b, 'OP_ASSIGN')], obj2)
		#prints the store statements
		print astToLLVM(obj1, a)
		print astToLLVM(obj2, b)
		#stores the operation result in temp var c
		print "	 "+c+" = "+self.operation+" i32 "+a+", "+b
		#stores contents of c in x
		print "	 "+"store i32 "+c+", i32* "+self.assignTo+", align 4"

#class for operators (UnaryAdd and UnarySub)
class UnaryllvmOp:
	def __init__(self,n,op,x):
		self.operation = op
		self.exp = n
		self.assignTo = x
	def codegen(self):
		a = genSym()
		obj = load(self.exp,a)
		c = genSym()
		temp = Assign(AssName(a),obj)
		print astToLLVM(obj, a)
		print "	 "+c+" = "+self.operation+" i32 0, "+a
		print "	 "+"store i32 "+c+", i32* "+self.assignTo+", align 4"

class AugllvmOp:
	def __init__(self, n, op, x):
		self.operation = op
		self.exp = n
		self.assignTo = x
	def codegen(self):
		a = genSym()
		b = genSym()
		obj = load(self.exp,a)
		obj2 = load(self.assignTo,b)
		c = genSym()
		temp = Assign(AssName(a),obj)
		temp2 = Assign(AssName(b),obj2)
		print astToLLVM(obj, a)
		print astToLLVM(obj2,b)
		print "	 "+c+" = "+self.operation+" i32 "+b+", "+a
		print "	 "+"store i32 "+c+", i32* "+self.assignTo+", align 4"

class Printllvm:
	def __init__(self, n, x):
		self.assignTo = x
		self.exp = n
	def codegen(self):
		a = genSym()
		b = genSym()
		obj = load(self.exp,a)
		temp = Assign(AssName(a),obj)
		print astToLLVM(obj,a)
		print "	 "+b+" = call i32 @print_int_nl(i32 "+a+") "
		
class PowllvmOp:
	def __init__(self,l,r,x):
		self.left = l
		self.right = r
		self.assignTo = x
	def codegen(self):
		a = genSym()
		b = genSym()
		c = genSym()
		d = genSym()
		e = genSym()
		f = genSym()
		obj1 = load(self.left, a)
		print astToLLVM(obj1,a)
		print "	 "+c+" = sitofp i32 "+a+" to double"
		obj2 = load(self.right, b)
		print astToLLVM(obj2, b)
		print "	 "+d+" = sitofp i32 "+b+" to double"
		print "	 "+e+" = call double @llvm.pow.f64(double "+c+","+" double "+d+")"
		print "	 "+f+" = fptosi double "+e+" to i32"
		print "	 "+"store i32 "+f+", i32* "+self.assignTo+", align 4"



class FloorllvmOp:
	def __init__(self,l,r,x):
		self.left = l
		self.right = r
		self.assignTo = x
	def codegen(self):
		a = genSym()
		b = genSym()
		obj1 = load(self.left, a)
		obj2 = load(self.right, b)
		#temporary variable to store the operation before it can be stored in x
		c = genSym()
		#prints the store statements
		print astToLLVM(obj1, a)
		print astToLLVM(obj2, b)
		print "	 "+c+" = sdiv i32 "+a+", "+b
		f = genSym()
		print "	 "+f+" = sitofp i32 "+c+" to double"
		d = genSym()
		e = genSym()
		print "	 "+d+" = call double @floor(double "+f+") nounwind readnone"
		print "	 "+e+" = fptosi double "+d+" to i32"
		print "	 "+"store i32 "+e+", i32* "+self.assignTo+", align 4"
		
	
		
		
#class for constants
class constant:
	def __init__(self, c):
		self.val = c.value;
		self.toString = str(self.val)



#a load class to make printing the load instruction easier
#tentative TODO: maybe make a class for store instructions as well?
#just for the sake of consistency. or not. whatever.
class load:
	def __init__(self, var,a):
		self.toString = "	 "+a+" = load i32* "+ var+", align 4"


	

#calls compile to start the program
compile()







		

