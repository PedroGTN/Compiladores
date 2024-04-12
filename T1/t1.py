import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from VisitorInterp import VisitorInterp
from ListenerInterp import ListenerInterp

archive_input, archive_out = sys.argv[1:]

def traverse(tree, rule_names, indent = 0):
    if tree.getText() == "<EOF>":
        return
    elif isinstance(tree, TerminalNode):
        print("{0}TOKEN='{1}'".format("  " * indent, tree.getText()))
    else:
        print("{0}{1}".format("  " * indent, rule_names[tree.getRuleIndex()]))
        for child in tree.children:
            traverse(child, rule_names, indent + 1)

input_string = FileStream(archive_input)
lexer = ExprLexer(input_string)
stream = CommonTokenStream(lexer)
parser = ExprParser(stream)
tree = parser.start_()
traverse(tree, parser.ruleNames)


