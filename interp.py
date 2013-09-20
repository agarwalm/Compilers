import compiler
from compiler.ast import *
import sys


filePath = sys.argv[1]

ast = compiler.parseFile(filePath)

print ast

