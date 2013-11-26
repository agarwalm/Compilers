#Homework 3 Compiler
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola
#Use Python version 2

import sys
import operator
import os
import a3test
from AstClasses import *
import compiler


#keeps track of the current variable in use so they can be incremented
#by genSym()
varName = 4

#keeps track of the current label num in use so that they can be generated
labelnum = 0
# env sumbol
envVarName = 0

#the list of flattened statement nodes
flatStmts = []
variables = []

nested_if = False
or_if = False
currentEnd = None
nested_or = False
endCount = 0;

endLab = "END"

#gets creates an ast from the contenst of a file name given as an argument
#generates LLVM code from the contents of the file
def compile():
	#check that the user has given exactly one file as input
	assert(len(sys.argv) == 2);
	
	#the file to interpret is the first argument given
	filePath = sys.argv[1]
	#abstract syntax tree for the contents of the file
	ast=a3test.getAST()
	print "\n\n; ",ast
	print " "
	
	print "\n\n;i am freeVars",free_vars(ast)
	d = closureConversion(ast)
	ast = d
	print "\n\n; converted ast: ", ast, "\n"
	e = lambdaLifting(ast)
	print "\n\n; lifted ast: ", e, "\n"
	ast = e
	
	for k in lambdaAssigns.keys():
		lambdaAssigns[k] = boxingPass(lambdaAssigns[k])
	
	print "\n\n; tagged dict: ", lambdaAssigns
	
	
	
	#ast2 = compiler.parseFile(filePath)
	#print ast2

	
	
	#this is where the tagging happens
	boxingPass(ast);

	print "\n\n; THE TAGGED AST: ", ast
	
	
#	print "; ",ast
#	print " "
	
	#this is where the flattening happens
	flatten(ast)
	
#	for s in flatStmts:
#		print "; ",s
#	
#	print " "
	
	
	
	#	print '@.str = private unnamed_addr constant [3 x i8] c"%d\\00", align 1'
	#	print '@.str1 = private unnamed_addr constant [4 x i8] c"%d\\0A\\00", align 1'
	#	print 'define i32 @input() nounwind uwtable ssp { '
	
	
	print 'declare i32 @input() nounwind uwtable ssp '
	
	
	#	print '  %n = alloca i32, align 4'
	#	print '  %1 = call i32 (i8*, ...)* @scanf(i8* getelementptr inbounds ([3 x i8]* @.str, i32 0, i32 0), i32* %n)'
	#	print '  %2 = load i32* %n, align 4'
	#	print '  ret i32 %2'
	#	print '}\n'
	#	print 'declare i32 @scanf(i8*, ...)\n'
	
	
	print 'declare i32 @print_int_nl(i32 %x) nounwind uwtable ssp '
	
	#	print 'define i32 @print_int_nl(i32 %x) nounwind uwtable ssp { '
	#	print '  %1 = alloca i32, align 4'
	#	print '  store i32 %x, i32* %1, align 4'
	#	print '  %2 = load i32* %1, align 4'
	#	print '  %3 = call i32 (i8*, ...)* @printf(i8* getelementptr inbounds ([4 x i8]* @.str1, i32 0, i32 0), i32 %2)'
	#	print '  ret i32 0'
	#	print '}\n'
	#	print 'declare i32 @printf(i8*, ...)'
	
	
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


def free_vars(n):
	
	if isinstance(n, Module):
		
		return free_vars(n.nodes)
	
	
	elif isinstance(n,Stmt):
		templist = []
		for x in n.nodes:
			templist += free_vars(x)
		return templist
	
	
	
	elif isinstance(n, Discard):
		return free_vars(n.expr)
	
	elif isinstance(n, Assign):
		return free_vars(n.expr)
	
	
	elif isinstance(n, Printnl):
		temp = []
		for n in n.nodes:
			temp+=free_vars(n)
		return temp
	
	
	elif isinstance(n, Const) or isinstance(n, Bool):
		return set([])
	
	elif isinstance(n, Name):
		return set([n.name])
	
	elif isinstance(n, Add):
		return free_vars(n.left) | free_vars(n.right)
	
	elif isinstance(n, CallFunc):
		fv_args = [free_vars(e) for e in n.args]
		free_in_args = reduce(lambda a, b: a | b, fv_args, set([]))
		return free_vars(n.node) | free_in_args

	elif isinstance(n, Return):
		return free_vars(n.value)
		
	
	elif isinstance(n, Lambda):
		templist = []
		tempbound = []
		for frag in n.code:
			a = free_vars(frag)
			b = bounded_vars(frag)
			if a!= None:
				templist += free_vars(frag)
			if b != None:
				tempbound += bounded_vars(frag)
		return set(templist) - (set(tempbound) | set(n.argnames))
	
	elif isinstance(n, ConvertedLambda):
		return free_vars(n.code) - AssName(n)
	
	elif isinstance(n, Return):
		return set([])
	
	
	else:
		
		print "hello what the hell!!!"



def bounded_vars(n):
	
	if isinstance(n, Module):
		
		return bounded_vars(n.nodes)
	
	
	elif isinstance(n,Stmt):
		templist = []
		for x in n.nodes:
			templist += bounded_vars(x)
		return templist
	

	
	elif isinstance(n, Assign):
		return set([n.name])
	
	
	elif isinstance(n, Lambda):
		templist = []
		for frag in n.code:
			templist += bounded_vars(frag)
		return set(templist) | set(n.argnames)
	
	elif isinstance(n, ConvertedLambda):
		return free_vars(n.code) - AssName(n.name)
	
	elif isinstance(n, Return):
		return set([])
	
	
	else:
		print "hello what the hell!!!"




def closureConversion(n):
	if isinstance(n, Module):
		d = Module(closureConversion(n.nodes))
		return d
	
	
	elif isinstance(n,Stmt):
		convertedNodes = []
		for x in n.nodes:
			convertedNodes.append(closureConversion(x))
		return Stmt(convertedNodes)
	
	elif isinstance(n, Discard):
		d = Discard(closureConversion(n.expr))
		return d
	
	elif isinstance(n, Assign):
		d = Assign(n.name,closureConversion(n.expr))
		return d

	elif isinstance(n,Return):
		d = Return(closureConversion(n.expr))
		return d
	
	elif isinstance(n, Lambda):
		a = free_vars(n)
		env = makeEnvVar()
		make_env = {}
		for vars in a:
			key = genSymFromVar(vars)
			#value = vars
			value = Name(vars)
			make_env[key] = value
		
		#freeVars = free_vars(n.code)
		#
		#
		#for vars in freeVars:
		#	vars = EnvRef(env, vars.name)
		#sub = [(vars.name, EnvRef(env, vars.name))]
		
		#TODO n.code is something else..need to use sub
		tempBody = []
		for c in n.code:
			tempBody.append(newBodyPass(env, a, c))
		b = ConvertedLambda(env, n.argnames, tempBody)

		d = MakeClosure(b, MakeEnv(make_env))
		return d
	else:
		return n


def newBodyPass(env, a, n):
	if isinstance(n, Discard):
		d = Discard(newBodyPass(env, a, n.expr))
		return d 
	elif isinstance(n, Const):
		return n
	elif isinstance(n, Add):
		n.left = newBodyPass(env, a, n.left)
		n.right = newBodyPass(env, a, n.right)
		return n
	
	elif isinstance(n, Sub):
		n.left = newBodyPass(env, a, n.left)
		n.right = newBodyPass(enc, a, n.right)
		return n
	
	elif isinstance(n, Mul):
		n.left = newBodyPass(env, a, n.left)
		n.right = newBodyPass(env, a, n.right)
		return n

	elif isinstance(n, Return):
		n.value = newBodyPass(env, a, n.value)
		return n

	elif isinstance(n, Assign):
		d = Assign(n.name, newBodyPass(env, a, n.expr))
		return d

	elif isinstance(n, Lambda):
		n =  closureConversion(n)
		return n
	
	
	elif isinstance(n, Name):
		if n.name in a:
			n = EnvRef(env, n.name)
		return n

	else:
		return n

lambdaAssigns = {}

def lambdaLifting(n):
	
	if isinstance(n, Module):
		n.nodes = lambdaLifting(n.nodes)
		return n

	elif isinstance(n, Stmt):
		tempNodes = []
		for i in n.nodes:
			tempNodes.append(lambdaLifting(i))
		return Stmt(tempNodes)

	elif isinstance(n, Discard):
		n.expr = lambdaLifting(n.expr)
		return n
		

	elif isinstance(n, Assign):
		if isinstance(n.expr,MakeClosure) :
			a = genSym()
			ident = n.name.name
			tempCode = []
			for i in n.expr.fun.code:
				tempCode.append(lambdaLifting(i))
			n.expr.fun.code = tempCode
			lambdaAssigns[ident] = n.expr.fun
			n.expr.fun = Name(n.name.name)
			n.name.name = a
			return n
		else:
			return n

	elif isinstance(n, MakeClosure):
		a = genSym()
		tempCode = []
		for i in n.fun.code:
			tempCode.append(lambdaLifting(i))
		n.fun.code = tempCode
		lambdaAssigns[a] = n.fun
		n.fun = Name(a)
		return n
	
	else:
		return n
	
			
	

#	elif isinstance(n, ConvertedLambda):
#		a = genSym()
#		n.code = lambdaLifting(n.code)
#		lambdaAssigns[a] = ConvertedLambda(n.env, n.argnames, n.code)
#		return Name(a)

	

		
	


#def lambdaLifting(n):
#	if isinstance(n, Module):
#	lambdaLifting(n.nodes)
#	return n
#		
#		
#	elif isinstance(n,Stmt):
#		for x in n.nodes:
#			lambdaLifting(x)
#		return n
#	
#	elif isinstance(n, Discard):
#		return lambdaLifting(n.expr)
#	
#	elif isinstance(n, Assign):
#		return lambdaLifting(n.expr)
#	
#	elif isinstance(n, Lambda):
#		a = free_vars(n)
#		env = makeEnvVar()
#		make_env = {}
#		for vars in a:
#			key = genSymFromVar(vars)
#			#value = vars
#			value = Name(vars)
#			make_env[key] = value
#		
#		#freeVars = free_vars(n.code)
#		#
#		#
#		#for vars in freeVars:
#		#	vars = EnvRef(env, vars.name)
#		#sub = [(vars.name, EnvRef(env, vars.name))]
#		
#		#TODO n.code is something else..need to use sub
#		for c in n.code:
#			newBodyPass(env, a, c)
#		b = ConvertedLambda(env, n.argnames, n.code)
#		return MakeClosure(b, MakeEnv(make_env))
#	else:
#		print "cannot apply closure conversion algorithm"
	



#adds necessary boxing and unboxing instructions to the ast
def boxingPass(n):
	
	if isinstance(n, Module):
		boxingPass(n.nodes)
		return n
	
	
	elif isinstance(n,Stmt):
		for x in n.nodes:
			boxingPass(x)
		return n
	
	elif isinstance(n, Discard):
		n.expr = boxingPass(n.expr)
		return n

	elif isinstance(n, MakeClosure):
		n.fun = boxingPass(n.fun)
		temp = Tag(n, "closure")
		n = temp
		return n

	elif isinstance(n, ConvertedLambda):
		tempCode = []
		for c in n.code:
			tempCode.append(boxingPass(c))
		n.code = tempCode
		return n
	
	elif isinstance(n,Const):
		if not isinstance(n.value, int):
			sys.exit('ERROR! All constants must be integer values')
		
		#check here to make sure the integer is not loger than 30 bits
		if n.value.bit_length() > 30:
			sys.exit('ERROR! Integers cannot be longer than 30 bits')
		#to Tag, create a Tag object with int flag because we tag ints differently than
		#booleans. The actual tagging occurs at runtime
		temp = Tag(n, "int")
		n = temp
		return n
	
	elif isinstance(n, Name):
		return n
	
	elif isinstance(n, Not):
		tagged = Tag( Bitxor( ConvertToInt ( boxingPass( BoolExp(n.expr, "!=", Const(0), "") ) ), ConvertToInt( Tag( Bool(1,""), "bool") )), "bool" )
		tagged.flag = "bool"
		return tagged

	elif isinstance(n, Return):
		n.value = boxingPass(n.value)
		return n
	
	
	
	elif isinstance(n,BoolExp):
		
		
		if (n.op == "and") or (n.op == "or"):
			#a boolean expression should untag each side of the boolean operator and then
			#tag the result
			tempL = boxingPass(n.left)
			tempR = boxingPass(n.right)
			#untag all by shifting left 2 (booleans treated as integers in this case)
			n.left = tempL
			n.right = tempR
			#to Tag, create a Tag object with bool flag because we tag ints differently than
			#booleans. The actual tagging occurs at runtime
			#the result will always be a boolean
			box = n
			return box
		
		else:
			#a boolean expression should untag each side of the boolean operator and then
			#tag the result
			tempL = boxingPass(n.left)
			tempR = boxingPass(n.right)
			#untag all by shifting left 2 (booleans treated as integers in this case)
			n.left = ConvertToInt(tempL)
			n.right = ConvertToInt(tempR)
			#to Tag, create a Tag object with bool flag because we tag ints differently than
			#booleans. The actual tagging occurs at runtime
			#the result will always be a boolean
			box = Tag(n, "bool")
			return box
	
	elif isinstance(n, AugAssign):
		expression = boxingPass(n.exp)
		n.exp = expression
		return n
	
	elif isinstance(n, UnarySub) or isinstance(n,UnaryAdd):
		expression = boxingPass(n.expr)
		n.expr = expression
		return n
	
	elif isinstance(n, Invert):
		n.expr = boxingPass(n.expr)
		return n
	
	
	
	elif isinstance(n, Bool):
		#tag as a bool
		temp = Tag(n, "bool")
		return temp
	
	
	elif isinstance(n,Assign):
		if not isinstance(n.name, AssName): #or len(n.nodes)>1:
			sys.exit('Tuple assignment not permitted')
		else:
			n.expr = boxingPass(n.expr)
			return n
	
	elif isinstance(n,Add) or isinstance(n,Div) or isinstance(n,Sub) or isinstance(n,Mul) or isinstance(n, LeftShift) or isinstance(n, RightShift) or isinstance(n,Power) or isinstance(n, Mod) or isinstance(n, FloorDiv):
		#if the left and right are integers, they will be boxed.
		#if they are names, their values have already been boxed.
		tempL = boxingPass(n.left)
		tempR = boxingPass(n.right)
		#to unbox, shift right by 2 for both bools and ints
		n.left= ConvertToInt(tempL)
		n.right = ConvertToInt(tempR)
		#the result will be an int, so tag as int
		box = Tag(n, "int")
		return box
	
	elif isinstance(n, Bitor) or isinstance(n, Bitand) or isinstance(n, Bitxor):
		tempL = boxingPass(n.left)
		tempR = boxingPass(n.right)
		if isinstance(n.left,Bool):
			n.left=ConvertToBool(tempL)
		else:
			n.left=ConvertToInt(tempL)
		if isinstance(n.right,Bool):
			n.right=ConvertToInt(tempR)
		else:
			n.right=ConvertToInt(tempR)
		
		box=Tag(n,"int")
		return box
	
	elif isinstance(n, IfNode):
		n.expr = boxingPass(n.expr)
		for i in range(0,len(n.nodes)):
			n.nodes[i] = boxingPass(n.nodes[i])
		if isinstance(n.alt, IfNode):
			boxingPass(n.alt)
		else:
			for i in range(0,len(n.alt)):
				n.alt[i] = boxingPass(n.alt[i])
		return n
	
	elif isinstance(n, WhileNode):
		n.expr = boxingPass(n.expr)
		for i in range(0,len(n.nodes)):
			n.nodes[i] = boxingPass(n.nodes[i])
		return n
	
	elif isinstance(n, Printnl):
		if (len(n.nodes) != 1):
			sys.exit('Print accepts a single integer value')
		n.nodes[0] = boxingPass(n.nodes[0])
		#When you untag before printing, you will have to check at runtime whether
		#the value being printed is an int or a bool, so you print the right thing
		#the Untag object (as opposed to ConvertToInt and ConvertToBool) could be
		#untagging either a boolean or an integer
		n.nodes[0] = n.nodes[0]
		return n







#takes a non flattened ast and returns a flattened ast
def flatten(n):
	
	if isinstance(n, Module):
		flatten(n.nodes)
	#iterate through all of the statement nodes
	elif isinstance(n, Stmt):
		global if_or
		for x in n.nodes:
			if_or = False
			flattenStmt(x)

def flattenStmt(n):
	#if you have an Assign, then use the given variable to assign
	#to the expression
	if isinstance(n, Assign):
		if not isinstance(n.name, AssName): #or len(n.nodes)>1:
			sys.exit('Tuple assignment not permitted')
		
		if isinstance(n.expr, Name):
			x = genSymFromVar(n.name.name)
			temp = Assign(AssName(x),Name(flattenExp(n.expr,genSym())))
			variables.append(x)
			flatStmts.append(temp)
		
		else:
			variables.append(genSymFromVar(n.name.name))
			flattenExp(n.expr, genSymFromVar(n.name.name))
	
	#if you have a discard, then generate a variable to assign
	#to the expression
	elif isinstance(n, Discard):
		flattenExp(n.expr, genSym())
	
	elif isinstance(n, Printnl):
		if (len(n.nodes) != 1):
			sys.exit('Print accepts a single integer value')
		a = genSym()
		variables.append(a)
		b = genSym()
		variables.append(b)
		
		t1 = Name(flattenExp(n.nodes[0], a))
		n.nodes[0] = t1;
		
		
		temp = Assign(AssName(b), n)
		flatStmts.append(temp)
		#		flatStmts.append(GoTo(ge))
		#flatStmts.append(Label(ge))
		return b
	
	elif isinstance(n, AugAssign):
		a = genSym()
		if isinstance(n.exp, Name):
			a = genSymFromVar(n.exp.name)
		flattened_expr = flattenExp(n.exp, a)
		x = genSymFromVar(n.name.name)
		variables.append(x)
		variables.append(flattened_expr)
		
		if(n.op == "+="):
			
			flattenExp(boxingPass(Add(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "-="):
			
			flattenExp(boxingPass(Sub(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "*="):
			
			flattenExp(boxingPass(Mul(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "/="):
			
			flattenExp(boxingPass(Div(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "**="):
			
			flattenExp(boxingPass(Power(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "%="):
			
			flattenExp(boxingPass(Mod(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "<<="):
			
			flattenExp(boxingPass(LeftShift(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == ">>="):
			
			flattenExp(boxingPass(RightShift(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "&="):
			
			flattenExp(Bitand(LeftShift(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "|="):
			
			flattenExp(boxingPass(Bitor(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "^="):
			
			flattenExp(boxingPass(Bitxor(Name(x), Name(flattened_expr))), x)
		
		elif(n.op == "//="):
			
			flattenExp(boxingPass(FloorDiv(Name(x), Name(flattened_expr))), x)
	
	
	#n.exp = Name(a)
	
	#			if n.name.name not in variables:
	#				sys.exit('ERROR! Use of undefined variable '+n.name.name)
	#			n.name = Name(x)
	#			temp = Assign(AssName(x),add)
	#			flatStmts.append(temp)
	
	
	
	elif isinstance(n, IfNode):
		#we will modify the IfNode to form first line of the example in the notes:
		#If not cond goto F:
		n.expr = flattenExp(n.expr, genSym())
		f = genLabel("F")
		t = genLabel("T")
		gotof = GoTo(f)
		nodes = n.nodes
		elsestmts = n.alt
		
		tfIf = IfNode(n.expr, gotof, GoTo(t), "")
		
		flatStmts.append(tfIf)
		flatStmts.append(Label(t))
		#flatten the statements from the original true block
		for i in range(0, len(nodes)):
			d = flattenStmt(nodes[i])
		
		#generate a goto END for when you execute the true block and want to skip the else
		global endLab
		e = endLab
		
		if isinstance(elsestmts, IfNode):
			flatStmts.append(GoTo(e))
			flatStmts.append(Label(f))
			flattenStmt(elsestmts)
		
		
		
		#tfIf.nodes = GoTo(b)
		
		else:
			
			if len(elsestmts) >0:
				gotoe = GoTo(e)
				flatStmts.append(gotoe)
				#label F for the false block
				falselabel = Label(f)
				flatStmts.append(falselabel)
				n.alt = gotof
				#flatten the statements from the original false block
				for i in range(0, len(elsestmts)):
					if isinstance(elsestmts[i], IfNode):
						global nested_if
						nested_if = True;
					flattenStmt(elsestmts[i])
			
			#flatStmts.append(gotoe)
			
			
			
			
			else:
				tfIf.nodes = GoTo(e)
			
			global nested_if
			global if_or
			if nested_if == False and n.flag != "or":
				print "; don't print end!\n"
				
				flatStmts.append(GoTo(e))
				
				endLab = genLabel("END")
				
				
				#end label for the end of the if statement (where you jump to if the condition is true)
				endLabel = Label(e)
				flatStmts.append(endLabel)
				nested_if = False
			else:
				nested_if = False
	
	
	
	
	
	
	
	
	elif isinstance(n, WhileNode):
		
		b = genLabel("BOTTOM")
		end = genLabel("END")
		gotob = GoTo(b)
		
		flatStmts.append(gotob)
		t = genLabel("TOP")
		toplabel = Label(t)
		flatStmts.append(toplabel)
		
		for node in n.nodes:
			flattenStmt(node)
		
		flatStmts.append(GoTo(b))
		bottomlabel = Label(b)
		flatStmts.append(bottomlabel)
		n.expr = flattenExp(n.expr, genSym())
		ifcond = IfNode(n.expr, GoTo(end), GoTo(t), "")
		flatStmts.append(ifcond)
		flatStmts.append(GoTo(end))
		flatStmts.append(Label(end))
	
	
	
	
	else:
		print "; unrecognized: ", n
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
	elif isinstance(n,Name):
		a = genSymFromVar(n.name)
		if n.name not in variables and genSymFromVar(n.name) not in variables:
			sys.exit('ERROR! Use of undefined variable '+n.name)
		return a
	
	elif isinstance(n, Bool):
		temp = Assign(AssName(x), n)
		flatStmts.append(temp)
		return x
	
	
	elif isinstance(n, Tag) or isinstance(n,Untag) or isinstance(n, ConvertToBool) or isinstance(n, ConvertToInt):
		variables.append(genSymFromVar(x))
		if isinstance(n.node, Const):
			temp = Assign(AssName(x), n)
			flatStmts.append(temp)
			return x
		elif isinstance(n.node, Bool):
			temp = Assign(AssName(x), n)
			flatStmts.append(temp)
			return x
		else:
			a = genSym()
			n.node = Name(flattenExp(n.node,a))
			temp = Assign(AssName(x),n)
			flatStmts.append(temp)
			return x
	
	elif isinstance(n, Not):
		a = genSym()
		exp = flattenExp(n.expr, a)
		n.expr = exp
		temp = Assign(AssName(x), n)
		flatStmts.append(temp)
		return x
	
	
	elif isinstance(n,Add) or isinstance(n,Div) or isinstance(n,Sub) or isinstance(n,Mul) or isinstance(n, LeftShift) or isinstance(n, RightShift) or isinstance(n,Power) or isinstance(n, Mod) or isinstance(n, FloorDiv):
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
	
	elif isinstance(n,BoolExp):
		variables.append(genSymFromVar(x))
		
		if (n.op != 'and') and (n.op != 'or'):
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
		
		elif n.op == 'and':
			d = genSym()
			e = genSym()
			tempright = n.right
			#print "i am tempright", tempright
			templeft = n.left
			n.right = ConvertToInt(Tag(Const(0), "int"))
			n.left = ConvertToInt(n.left)
			n.op = "!="
			n.flag = "check"
			var = genSymFromVar(x)
			variables.append(var)
			a = genSym()
			b = genSym()
			print "; tr:",tempright
			flattenExp(tempright, a)
			print "; left:",templeft
			flattenExp(templeft, b)
			print "; got here!"
			r = Assign(AssName(var), Name(a))
			variables.append(a)
			
			l = Assign(AssName(var), Name(b))
			variables.append(b)
			
			g = genSym()
			print "; blah"
			print "; ", flatStmts
			print "; ifnode: ", IfNode(Tag(n, "bool"), [r], [l], "and" )
			andIf = flattenStmt(IfNode(Tag(n, "bool"), [r], [l], "and" ))
			print "; rawr"
			#flatStmts.append(andIf)
			
			return x
		
		
		
		elif n.op == 'or':
			#
			#			t = n.left.node.node
			#			r = n.right.node.node
			#global if_or
			#if_or = True;
			
			
			tempright = n.right
			templeft = n.left
			n.right = ConvertToInt(Tag(Const(0), "int"))
			n.left = ConvertToInt(n.left)
			n.op = "!="
			n.flag = "check"
			var = genSymFromVar(x)
			variables.append(var)
			
			a = genSym()
			b = genSym()
			
			print "; tr:",tempright
			flattenExp(tempright, a)
			print "; left:",templeft
			flattenExp(templeft, b)
			print "; got here!"
			
			r = Assign(AssName(var), Name(a))
			
			l = Assign(AssName(var), Name(b))
			
			orIf = flattenStmt(IfNode(Tag(n, "bool"), [l], [r], "or" ))
			
			e = specialEnd()
			flatStmts.append(GoTo(e))
			#end label for the end of the if statement (where you jump to if the condition is true)
			endLabel = Label(e)
			flatStmts.append(endLabel)
			global endCount
			endCount = 0;
			
			
			return x
	
	
	
	
	elif isinstance(n,UnarySub) or isinstance(n, UnaryAdd):
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
	
	elif isinstance(n, Bitand) or isinstance(n,Bitor) or isinstance(n, Bitxor):
		var = dict()
		lst = []
		#generate symbols and assign them to the first two
		#nodes of the bit operator
		a = genSym()
		b = genSym()
		flattened_exp1 = flattenExp(n.left, a)
		flattened_exp2 = flattenExp(n.right, b)
		
		#create the propper operation for the assignment
		if isinstance(n, Bitand):
			op = Bitand(Name(flattened_exp1),Name(flattened_exp2))
		elif isinstance(n, Bitor):
			op = Bitor(Name(flattened_exp1),Name(flattened_exp2))
		elif isinstance(n, Bitxor):
			op = Bitxor(Name(flattened_exp1),Name(flattened_exp2))
		
		#make the assignment to the bit operator needed and add it to the
		#flatStmts list
		temp = Assign(AssName(x),op)
		flatStmts.append(temp)
		
		#if you only have 2 operands,
		#add the assignment to the flatStmts list
		#note: the constant assignments were already made when you
		#called flattenExp on n.nodes[0] and n.nodes[1]
		#if len(n.nodes)==2:
		return x
	
	elif isinstance(n, Invert):
		a = genSym()
		variables.append(a)
		
		b = genSym()
		variables.append(b)
		flattened_expr = flattenExp(n.expr, a)
		t1 = Name(flattened_expr)
		#		n.expr = t1
		#		temp = Assign(AssName(x),n)
		#		flatStmts.append(temp)
		#		return x
		
		flattenExp(boxingPass(Add(t1,Const(1))),b)
		flattenExp(boxingPass(Sub(Const(0),Name(b))),x)
		return x
	
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
		print flatStmts
		print n
		sys.exit('I am an unrecognized AST')

def makeEnvVar():
	global envVarName
	name = 'env'+ str(envVarName)
	envVarName += 1
	return name

#generate a F label
def genLabel(s):
	global labelnum
	name = s+str(labelnum)
	labelnum += 1
	return name

#generates a unique variable name
def genSym():
	global varName
	name= '%.'+ str(varName)
	varName += 1
	return name


#make special END labels
def specialEnd():
	endCount +=1
	global endLab
	global endCount
	e = endLab*endCount
	endLab = genLabel("END")
	return e



#adds a % infront of a given variable name to generate
#an llvm-friendly variable
def genSymFromVar(v):
	if v[0]=="%":
		return v
	vStr = "%."+v
	return vStr

#prints all alloca instructions for the variables in the flatStmts list
def alloc():
	
	lst = []
	for element in flatStmts:
		if isinstance(element, Assign) and element.name.name not in lst:
			lst.append(element.name.name)
	
	for element in lst:
		print "	 "+element + " = alloca i32, align 4"
		variables = lst


current_ifcheck = None


#generates llvm code from the Assign statements in the flatStmts list
def astToLLVM(ast, x):
	
	
	if isinstance(ast, Assign):
		#if the assign statement has only one constant or name to the right of the equals sign, output a store instruction
		if isinstance(ast.expr, Const):
			codegen_assign_const(ast, ast.name.name)
		
		if isinstance(ast.expr, Bool):
			codegen_assign_bool(ast,ast.name.name)
		
		
		if isinstance(ast.expr, Name):
			codegen_assign_name(ast)
		
		#otherwise it means there is a more complex expression to the right of the equals sign
		#we need to go deeper
		else:
			astToLLVM(ast.expr, ast.name.name)
	
	elif isinstance(ast, Special):
		print ast.str1+current_ifcheck+ast.str2
	
	elif isinstance(ast, ZSpecial):
		print ast.str
	
	elif isinstance(ast, Const):
		return str(ast.value)
	
	elif isinstance(ast, Bool):
		return str(ast.value)
	
	elif isinstance(ast, BoolExp):
		return codegen_boolExp(ast, x, ast.flag)
	
	elif isinstance(ast, Tag):
		return codegen_tag(ast, x)
	
	elif isinstance(ast, ConvertToInt):
		return codegen_toint(ast,x)
	
	elif isinstance(ast, ConvertToBool):
		return codegen_tobool(ast,x)
	
	elif isinstance(ast, IfNode):
		return codegen_if(ast,genSym())
	
	elif isinstance(ast, Label):
		return codegen_label(ast)
	
	elif isinstance(ast, GoTo):
		print "     br label %"+ast.label
	
	
	elif isinstance(ast, Add):
		return codegen_binop(ast,x, "add")
	
	elif isinstance(ast, Sub):
		return codegen_binop(ast,x,"sub")
	
	elif isinstance(ast, Mul):
		return codegen_binop(ast,x, "mul")
	
	elif isinstance(ast, Div):
		return codegen_binop(ast,x,"sdiv")
	
	
	elif isinstance(ast, Mod):
		return codegen_binop(ast,x, "srem")
	
	elif isinstance(ast, LeftShift):
		return codegen_binop(ast,x,"shl")
	
	elif isinstance(ast, RightShift):
		return codegen_binop(ast,x, "ashr")
	
	elif isinstance(ast, FloorDiv):
		return codegen_floordiv(ast,x)
	
	elif isinstance(ast, Power):
		return codegen_power(ast,x)
	
	
	elif isinstance(ast, Bitor):
		return codegen_binop(ast,x, "or")
	
	elif isinstance(ast, Bitand):
		return codegen_binop(ast,x, "and")
	
	elif isinstance(ast, Bitxor):
		return codegen_binop(ast,x, "xor")
	
	elif isinstance(ast, AssName):
		return ast.name
	
	elif isinstance(ast, Name):
		return ast.name
	
	elif isinstance(ast, UnarySub):
		return codegen_unary(ast,x,"us")
	
	elif isinstance(ast, UnaryAdd):
		return codegen_unary(ast,x,"ua")
	elif isinstance(ast, Not):
		return codegen_not(ast, x)
	
	elif isinstance(ast, Invert):
		return codegen_invert(ast,x)
	
	elif isinstance(ast, AugAssign):
		return codegen_augassign(ast,ast.name.name,ast.op)
	
	elif isinstance(ast, Printnl):
		return codegen_print(ast, x)
	
	elif isinstance(ast, CallFunc):
		return codegen_callfunc(ast, x)
	
	else:
		
		sys.exit('io sono an unrecognized AST')




#THE LLVM CODE GENERATION METHODS


def codegen_assign_const(ast,x):
	print"\n ; storing ", ast.expr.value," in ",x,"\n"
	output_store(str(ast.expr.value),x)

def codegen_assign_bool(ast,x):
	print"\n ; assigning boolean  ", ast.expr," to ",x,"\n"
	
	val = astToLLVM(ast.expr,x)
	if ast.expr.flag == "check":
		
		print"\n ; boolean,  ", ast.expr," is a check in an IfNode \n"
		
		global current_ifcheck
		a = genSym();
		print "	 "+a + " = alloca i1, align 4"
		output_istore(val,a)
		b = genSym()
		output_iload(b,a)
		current_ifcheck = b
	
	else:
		output_store(val,x)


def codegen_tag(ast,x):
	
	print"\n ; Tagging ",x,"\n"
	
	c = genSym()
	#	print "	 "+c + " = alloca i32, align 4"
	if isinstance(ast.node, Const):
		output_store(str(ast.node.value),x)
		#	output_store(c,x)
		a = genSym();
		print "	 "+a + " = alloca i32, align 4"
		output_store(str(2),a)
		
		astToLLVM(LeftShift(Name(x), Name(a)), x)
		if ast.flag == "int":
			return
		elif ast.flag == "bool":
			b = genSym()
			print "	 "+b + " = alloca i32, align 4"
			output_store(str(1),b)
			astToLLVM(Bitor(Name(x), Name(b)), x)
	
	if isinstance(ast.node, Bool):
		d = genSym()
		output_store(str(ast.node.value),x)
		
		if ast.node.flag == "check":
			print"\n ; boolean,  ", ast.node," is a check in an IfNode \n"
			p = genSym()
			e = genSym()
			print "	 "+p + " = alloca i32, align 4"
			output_load(e,x)
			output_store(e,p)
			global current_ifcheck
			current_ifcheck = p
		
		#output_store(d,x)
		#	output_store(c,x)
		a = genSym();
		print "	 "+a + " = alloca i32, align 4"
		output_store(str(2),a)
		
		astToLLVM(LeftShift(Name(x), Name(a)), x)
		if ast.flag == "int":
			return
		elif ast.flag == "bool":
			b = genSym()
			print "	 "+b + " = alloca i32, align 4"
			output_store(str(1),b)
			astToLLVM(Bitor(Name(x), Name(b)), x)
		
		
		if ast.node.flag == "check":
			q = genSym()
			k = genSym()
			
			output_load(q,current_ifcheck)
			print "	 "+k+" = trunc i32 "+q+" to i1"
			current_ifcheck = k
			print " "
	
	else:
		
		d = astToLLVM(ast.node,x)
		#	output_store(c,x)
		a = genSym();
		print "	 "+a + " = alloca i32, align 4"
		output_store(str(2),a)
		
		astToLLVM(LeftShift(Name(d), Name(a)), x)
		if ast.flag == "int":
			return
		elif ast.flag == "bool":
			b = genSym()
			print "	 "+b + " = alloca i32, align 4"
			output_store(str(1),b)
			astToLLVM(Bitor(Name(x), Name(b)), x)

def codegen_print(ast,x):
	print"\n ; generating code to print,  ", x ," \n"
	a = genSym()
	b = genSym()
	output_load(a,ast.nodes[0].name)
	output_call(b,"i32","print_int_nl","i32"+a,"")

def codegen_tobool(ast,x):
	a = genSym();
	b = genSym();
	print " "
	print "	 "+a + " = alloca i32, align 4"
	output_store(str(2),a)
	astToLLVM(RightShift(Name(astToLLVM(ast.node, genSym())), Name(a)), x)

def codegen_toint(ast,x):
	print"\n ; Untagging,  ", ast.node ," \n"
	a = genSym();
	b = genSym();
	print " "
	print "	 "+a + " = alloca i32, align 4"
	output_store(str(2),a)
	astToLLVM(RightShift(Name(astToLLVM(ast.node, genSym())), Name(a)), x)


def codegen_assign_name(ast):
	a = genSym()
	output_load(a, ast.expr.name);
	output_store(a, ast.name.name)

def codegen_boolExp(ast,x, flag):
	
	print"\n ; generating code for boolean expression,  ", ast ," \n"
	
	a = genSym()
	b = genSym()
	output_load(a, astToLLVM(ast.left,x))
	output_load(b, astToLLVM(ast.right,x))
	c = genSym()
	d = genSym()
	if ast.op == "<":
		print  "  "+c+" = icmp slt i32 "+a+", "+b
	elif ast.op == ">":
		print  "  "+c+" = icmp sgt i32 "+a+", "+b
	elif ast.op == "==":
		print "   "+c+" = icmp eq i32 "+a+", "+b
	elif ast.op == "<=":
		print "   "+c+" = icmp sle i32 "+a+", "+b
	elif ast.op == ">=":
		print "   "+c+" = icmp sge i32 "+a+", "+b
	elif ast.op == "!=":
		print "   "+c+" = icmp ne i32 "+a+", "+b
	
	if flag == "check":
		global current_ifcheck
		current_ifcheck = c
	
	
	else:
		
		
		print "	 "+d+" = zext i1 "+c+" to i32"
		print " "
		output_store(d,x)



def codegen_if(ast,x):
	
	print"\n ; generating code for ,  ", ast ," \n"
	
	global current_ifcheck
	print "   br i1 "+current_ifcheck+", label "+"%"+ast.alt.label+", label "+"%"+ast.nodes.label
	print " "


def codegen_label(ast):
	#	if ast.name[0:-1] == "END":
	#		print "    br label %"+ast.name
	print " "
	print ast.name+":"
	print " "


def codegen_binop(ast,x, op):
	print"\n ; generating code for binry op ,  ", ast ," \n"
	#must create temporary variables for the load operations
	a = genSym()
	b = genSym()
	output_load(a, astToLLVM(ast.left,x))
	output_load(b, astToLLVM(ast.right,x))
	c = genSym()
	output_operation(c,a,b,op)
	#stores contents of c in x
	output_store(c,x)


def codegen_unary(ast,x, op):
	
	print"\n ; generating code unary op ,  ", ast ," \n"
	
	a = genSym()
	output_load(a, astToLLVM(ast.expr,x))
	c = genSym()
	if(op == 'us'):
		output_operation(c,"0",a,"sub")
	else:
		output_operation(c,"0",a,"add")
	output_store(c,x)

def codegen_invert(ast, x):
	
	print"\n ; generating code for invert ,  ", ast ," \n"
	
	a = genSym()
	output_load(a, astToLLVM(ast.expr, x))
	c = genSym()
	output_operation(c , a , "1" , "add")
	d = genSym()
	output_operation(d, "0", c , "sub" )
	output_store(d, x)

def codegen_floordiv(ast,x):
	
	print"\n ; generating code for floordiv ,  ", ast ," \n"
	
	a = genSym()
	b = genSym()
	c = genSym()
	output_load(a,astToLLVM(ast.left,x))
	output_load(b,astToLLVM(ast.right,x))
	output_operation(c,a,b,"sdiv")
	f = genSym()
	output_sitofp_todouble(f,c)
	d = genSym()
	e = genSym()
	output_call(d, "double", "floor", "double "+f, "nounwind readnone" )
	output_fptosi_double(e,d)
	output_store(e, x)

def codegen_power(ast,x):
	
	print"\n ; generating code for power ,  ", ast ," \n"
	
	a = genSym()
	b = genSym()
	c = genSym()
	d = genSym()
	e = genSym()
	f = genSym()
	output_load(a, astToLLVM(ast.left,x))
	output_sitofp_todouble(c,a)
	output_load(b, astToLLVM(ast.right,x))
	output_sitofp_todouble(d,b)
	output_call(e,"double","llvm.pow.f64","double "+c+","+" double "+d,"")
	output_fptosi_double(f,e)
	output_store(f,x)


#def codegen_not(ast, x):





def  codegen_augassign(ast, x, op):
	
	print"\n ; generating code for augassign ,  ", ast ," \n"
	
	e = astToLLVM(ast.exp, x)
	llvmop = None
	if(op == "+="):
		llvmop = "add"
	elif(op == "-="):
		llvmop = "sub"
	elif(op == "/="):
		llvmop = "sdiv"
	elif(op == "*="):
		llvmop = "mul"
	elif(op == "%="):
		llvmop = "srem"
	elif (op == "<<="):
		llvmop = "shl"
	elif (op == ">>="):
		llvmop = "ashr"
	elif (op == "&="):
		llvmop = "and"
	elif (op == "|="):
		llvmop = "or"
	elif (op == "^="):
		llvmop = "xor"
	elif (op == "**="):
		llvmop = "pow"
	elif (op == "//="):
		llvmop = "sdiv"
	a = genSym()
	b = genSym()
	output_load(a, e)
	output_load(b,x)
	c = genSym()
	output_operation(c,b,a,llvmop)
	output_store(c,x)

def codegen_callfunc(ast,x):
	
	print"\n ; calling the function ,  "+ ast.node.name +" \n"
	
	a = genSym()
	output_call(a,"i32",ast.node.name,"","")
	output_store(a,x)


def output_load(tempvar, val):
	print "	 "+tempvar+" = load i32* "+ val+", align 4"

def output_iload(tempvar, val):
	print "	 "+tempvar+" = load i1* "+ val+", align 4"

def output_store(val, var):
	print "  "+"store i32 "+val+", i32* " + var+", align 4"

def output_istore(val, var):
	print "  "+"store i1 "+val+", i1* " + var+", align 4"

def output_operation(a,b,c, op):
	print "	 "+a+" = "+op+" i32 "+b+", "+c

def output_sitofp_todouble(a,b):
	print "	 "+a+" = sitofp i32 "+b+" to double"

def output_fptosi_double(a,b):
	print "	 "+a+" = fptosi double "+b+" to i32"

def output_call(a,ret,func,param,nounwind):
	print "	 "+a+" = call "+ret+" @"+func+"("+param+") "+nounwind




#calls compile to start the program
compile()