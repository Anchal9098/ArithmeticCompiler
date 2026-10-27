from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from intermediate import IntermediateCodeGenerator
from evaluator import Evaluator
expression = input("Enter Expression : ")

lexer = Lexer(expression)

tokens = lexer.tokenize()

print("\nTOKENS")
print("----------------")

for token in tokens:
    print(token)

parser = Parser(tokens)

tree = parser.parse()

print("\nAST")
print("----------------")
print(tree)

semantic = SemanticAnalyzer()

semantic.analyze(tree)

print("\nSemantic Analysis Passed")