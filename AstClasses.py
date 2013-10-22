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

class Const:
	def __init__(self,value):
		self.value=value
	def __repr__(self):
		return "Const(%s)" % (self.value)
	def __str__(self):
		return "Const(%s)" % (self.value)

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
		return "Name()"
	def __str__(self):
		return "Name(%s)" % (self.name)

class Not:
	def __init__(self):
		self.expr=expr
	def __repr__(self):
		return "Not()"
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
		return "Print(%s)" % (self.nodes)
	def __str__(self):
		return "Print(%s)" % (self.nodes)

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
		return "UnaryAdd()"
	def __str__(self):
		return "UnaryAdd(%s)" % (self.expr)

class UnarySub:
	def __init__(self,expr):
		self.expr=expr
	def __repr__(self):
		return "UnarySub()"
	def __str__(self):
		return "UnarySub(%s)" % (self.expr)


