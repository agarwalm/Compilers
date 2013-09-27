#Homework 2 Compiler
#Mrigya Agarwal, Christine Graff, Giuseppe Mendola

import compiler
from compiler.ast import *
import sys
import operator

from llvm import *
from llvm.core import *

#the file to interpret is the first argument given 
filePath = sys.argv[1]

#abstract syntax tree for the contents of the file
ast = compiler.parseFile(filePath)

#dict to keep track of the mapping of variable names to stack slots
varToStack = {}


#takes a non flattened ast and returns a flattened ast
def flatten(exp, varName):






#TODO: after we have the flattened AST, we need to traverse it and generate LLVM code for each variable 





		

