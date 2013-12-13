# Mrigya Agarwal, Christine Graff, Giuseppe Mendola
#This file contains the implementation of our AST classes

class Module:
	def __init__(self, nodes):
		self.nodes = nodes
	def __repr__(self):
		return "Module()"
	def __str__(self):
		return "Module(%s)" % (self.nodes)


class Add:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Add(%s, %s)" % (self.left,self.right)
	def __str__(self):
		return "Add(%s, %s)" % (self.left,self.right)

class AssName:
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return "AssName(%s)" % (self.name)
	def __str__(self):
		return "AssName(%s)" % (self.name)

class Assign:
	def __init__(self, assname, exp):
		self.name = assname
		self.expr = exp
	def __repr__(self):
		return "Assign(%s, %s)" % (self.name, self.expr)
	def __str__(self):
		return "Assign(%s, %s)" % (self.name, self.expr)


class AugAssign:
	def __init__(self,name,op, exp):
		self.name=name
		self.op=op
		self.exp = exp
	def __repr__(self):
		return "AugAssign(%s, %s, %s)" % (self.name,self.op,self.exp)
	def __str__(self):
		return "AugAssign(%s, %s, %s)" % (self.name,self.op,self.exp)

class Bitand:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Bitand()"
	def __str__(self):
		return "Bitand(%s, %s)" % (self.left,self.right)

class Bitor:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Bitor()"
	def __str__(self):
		return "Bitor(%s, %s)" % (self.left,self.right)

class Bitxor:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Bitxor()"
	def __str__(self):
		return "Bitxor(%s, %s)" % (self.left,self.right)

class CallFunc:
	def __init__(self,node,args):
		self.node=node
		self.args=args
	def __repr__(self):
		return "CallFunc(%s,%s)"%(self.node,self.args)
	def __str__(self):
		return "CallFunc(%s,%s)" % (self.node,self.args)

class Const:
	def __init__(self,value,flag):
		self.value=value
		self.flag = flag
	def __repr__(self):
		return "Const(%s, %s)" % (self.value, self.flag)
	def __str__(self):
		return "Const(%s, %s)" % (self.value, self.flag)

class NoneNode:
	def __init__(self, value):
		self.value = value
	def __repr__(self):
		return "NoneNode()" 
	def __str__(self):
		return "NoneNode()"

class Discard:
	def __init__(self,expr):
		self.expr=expr
	def __repr__(self):
		return "Discard(%s)"% (self.expr)
	def __str__(self):
		return "Discard(%s)" % (self.expr)

class Div:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Div()"
	def __str__(self):
		return "Div(%s, %s)" % (self.left, self.right)

class FloorDiv:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "FloorDiv()"
	def __str__(self):
		return "FloorDiv(%s, %s)" % (self.left, self.right)

class Invert:
	def __init__(self,expr):
		self.expr=expr
	def __repr__(self):
		return "Invert()"
	def __str__(self):
		return "Invert(%s)" % (self.expr)


class LeftShift:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "LeftShift()"
	def __str__(self):
		return "LeftShift(%s, %s)" % (self.left, self.right)

class Mod:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Mod()"
	def __str__(self):
		return "Mod(%s, %s)" % (self.left, self.right)

class Mul:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Mul()"
	def __str__(self):
		return "Mul(%s, %s)" % (self.left, self.right)

class Name:
	def __init__(self,name):
		self.name=name
	def __repr__(self):
		return "Name(%s)" % (self.name)
	def __str__(self):
		return "Name(%s)" % (self.name)

class Not:
	def __init__(self, expr):
		self.expr=expr
	def __repr__(self):
		return"Not(%s)" % (self.expr)
	def __str__(self):
		return "Not(%s)" % (self.expr)

class Or:
	def __init__(self,nodes):
		self.nodes=nodes
	def __repr__(self):
		return "Or()"
	def __str__(self):
		return "Or(%s)" % (self.nodes)

class Power:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Power()"
	def __str__(self):
		return "Power(%s, %s)" % (self.left, self.right)

class Printnl:
	def __init__(self,nodes):
		self.nodes=nodes
	def __repr__(self):
		return "Printnl(%s)" % (self.nodes)
	def __str__(self):
		return "Printnl(%s)" % (self.nodes)

class Return:
	def __init__(self,value):
		self.value=value
	def __repr__(self):
		return "Return()"
	def __str__(self):
		return "Return(%s)" % (self.value)



class RightShift:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "RightShift()"
	def __str__(self):
		return "RightShift(%s, %s)" % (self.left, self.right)

class Stmt:
	def __init__(self,nodes):
		self.nodes=nodes
	def __repr__(self):
		return "Stmt(%s)" % (self.nodes)
	def __str__(self):
		return "Stmt(%s)" % (self.nodes)


class Sub:
	def __init__(self,l,r):
		self.right=r
		self.left=l
	def __repr__(self):
		return "Sub()"
	def __str__(self):
		return "Sub(%s, %s)" % (self.left, self.right)

class UnaryAdd:
	def __init__(self,expr):
		self.expr=expr
	def __repr__(self):
		return "UnaryAdd(%s)" % (self.expr)
	def __str__(self):
		return "UnaryAdd(%s)" % (self.expr)

class UnarySub:
	def __init__(self,expr):
		self.expr=expr
	def __repr__(self):
		return "UnarySub()"
	def __str__(self):
		return "UnarySub(%s)" % (self.expr)

class IfNode:
	def __init__(self,check,do,otherwise, flag):
		self.expr=check
		self.nodes = do
		self.alt = otherwise
		self.flag = flag
	def __repr__(self):
		return "IfNode(%s,%s,%s,%s)" % (self.expr, self.nodes, self.alt, self.flag)
	def __str__(self):
		return "IfNode(%s,%s,%s,%s)" % (self.expr, self.nodes, self.alt, self.flag)

class WhileNode:
	def __init__(self,check,do):
		self.expr=check
		self.nodes=do
	def __repr__(self):
		return "WhileNode(%s,%s)" % (self.expr, self.nodes)
	def __str__(self):
		return "WhileNode(%s,%s)" % (self.expr, self.nodes)
		

class BoolExp:
	def __init__(self,left,op,right,flag):
		self.left=left
		self.op = op
		self.right = right
		self.flag = flag
	def __repr__(self):
		return "BoolExp(%s,%s,%s,%s)" % (self.left,self.op, self.right,self.flag)
	def __str__(self):
		return "BoolExp(%s,%s,%s,%s)" % (self.left,self.op, self.right, self.flag)


class Bool:
	def __init__(self,val, flag):
		self.value = val
		self.flag = flag
	def __repr__(self):
		return "Bool(%s,%s)" % (self.value, self.flag)
	def __str__(self):
		return "Bool(%s,%s)" % (self.value, self.flag)

class Tag:
	def __init__(self,node,flag):
		self.node = node
		self.flag = flag
	def __repr__(self):
		return "Tag(%s, %s)" % (self.node, self.flag)
	def __str__(self):
		return "Tag(%s, %s)" % (self.node, self.flag)

class Untag:
	def __init__(self,node):
		self.node = node
	def __repr__(self):
		return "Untag(%s)" % (self.node)
	def __str__(self):
		return "Untag(%s)" % (self.node)

#untag as a boolean
class ConvertToBool:
	def __init__(self,node):
		self.node = node
	def __repr__(self):
		return "ConvertToBool(%s)" % (self.node)
	def __str__(self):
		return "ConvertToBool(%s)" % (self.node)

#untag as an int
class ConvertToInt:
	def __init__(self,node):
		self.node = node
	def __repr__(self):
		return "ConvertToInt(%s)" % (self.node)
	def __str__(self):
		return "ConvertToInt(%s)" % (self.node)

class GoTo:
	def __init__(self,label):
		self.label =  label
	def __repr__(self):
		return "GoTo(%s)" % (self.label)
	def __str__(self):
		return "GoTo(%s)" % (self.label)

class Label:
	def __init__(self,name):
		self.name =  name
	def __repr__(self):
		return "Label(%s)" % (self.name)
	def __str__(self):
		return "Label(%s)" % (self.name)

class Special:
	def __init__(self,str,s):
		self.str1 =  str
		self.str2 = s
	def __repr__(self):
		return "Special(%s,%s)" % (self.str1, self.str2)
	def __str__(self):
		return "Special(%s,%s)" % (self.str1, self.str2)

class ZSpecial:
	def __init__(self,str):
		self.str =  str
	def __repr__(self):
		return "ZSpecial(%s)" % (self.str)
	def __str__(self):
		return "ZSpecial(%s)" % (self.str)
	
class Function:
	def __init__(self,name, argnames, code):
		self.name = name
		self.argnames = argnames
		self.code = code
	def __repr__(self):
		return "Function(%s, %s, %s)" % (self.name, self.argnames, self.code)
	def __str__(self):
		return "Function(%s, %s, %s)" % (self.name, self.argnames, self.code)
			
	
class Lambda:
	def __init__(self, argnames, code):
		self.argnames = argnames
		self.code = code
	def __repr__(self):
		return "Lambda(%s, %s)" % (self.argnames, self.code)
	def __str__(self):
		return "Lambda(%s, %s)" % (self.argnames, self.code)
	
class Return():
	def __init__(self, value):
		self.value = value
	def __repr__(self):
		return "Return(%s)" % (self.value)
	def __str__(self):
		return "Return(%s)" % (self.value)
	#code

class ConvertedLambda():
	def __init__(self,env, argnames, code):
		self.env = env
		self.argnames = argnames
		self.code = code	
	def __repr__(self):
		return "ConvertedLambda(%s, %s, %s)" % (self.env, self.argnames, self.code)
	def __str__(self):
		return "ConvertedLambda( %s, %s, %s)" % (self.env, self.argnames, self.code)


class ConvertedFunction():
	def __init__(self,name, env, argnames, code):
		self.name = name
		self.env = env
		self.argnames = argnames
		self.code = code
	def __repr__(self):
		return "ConvertedLambda(%s,%s, %s, %s)" % (self.name, self.env, self.argnames, self.code)
	def __str__(self):
		return "ConvertedLambda(%s, %s, %s, %s)" % (self.name, self.env, self.argnames, self.code)
	
class MakeClosure():
	def __init__(self, fun, env):
		self.fun = fun
		self.env = env
	def __repr__(self):
		return "MakeClosure(%s, %s)" % (self.fun, self.env)
	def __str__(self):
		return "MakeClosure(%s, %s)" % (self.fun, self.env)

class CallFuncClosure():
	def __init__(self, fun, env):
		self.fun = fun
		self.env = env
	def __repr__(self):
		return "MakeClosure(%s, %s)" % (self.fun, self.env)
	def __str__(self):
		return "MakeClosure(%s, %s)" % (self.fun, self.env)

class MakeEnv():
	def __init__(self, map, name):
		self.map = map
		self.name = name
	def __repr__(self):
		return "MakeEnv(%s,%s)" % (self.map,self.name)
	def __str__(self):
		return "MakeEnv(%s,%s)" % (self.map, self.name)

class EnvRef():
	def __init__(self, env, name):
		self.env = env
		self.name = name
	def __repr__(self):
		return "EnvRef(%s, %s)" % (self.env, self.name)
	def __str__(self):
		return "EnvRef(%s, %s)" % (self.env, self.name)
	
class ApplyClosure():
	def __int__(self, closure, args):
		self.closure = closure
		self.args = args
	def __repr__(self):
		return "ApplyClosure(%s, %s)" % (self.closure, self.args)
	def __str__(self):
		return "ApplyClosure(%s, %s)" % (self.closure, self.args)

class Apply():
	def __init__(self, fun, args):
		self.fun = fun
		self.args = args
	def __repr__(self):
		return "Apply(%s, %s)" % (self.fun, self.args)
	def __str__(self):
		return "Apply(%s, %s)" % (self.fun, self.args)

class EOF():
	def __init__(self,val):
		self.val = val

	def __repr__(self):
		return "EOF()" 
	def __str__(self):
		return "EOF()"



	
		

	


	





