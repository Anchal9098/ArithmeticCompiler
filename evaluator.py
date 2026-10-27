from node import NumberNode, IdentifierNode, BinaryOperationNode


class Evaluator:

    def __init__(self):
        # Same values as semantic analyzer
        self.symbol_table = {
            "a": 10,
            "b": 20,
            "c": 30
        }

    def evaluate(self, node):

        # Number
        if isinstance(node, NumberNode):
            return node.value

        # Variable
        elif isinstance(node, IdentifierNode):
            return self.symbol_table[node.name]

        # Binary Operation
        elif isinstance(node, BinaryOperationNode):

            left = self.evaluate(node.left)
            right = self.evaluate(node.right)

            if node.operator.type == "PLUS":
                return left + right

            elif node.operator.type == "MINUS":
                return left - right

            elif node.operator.type == "MULTIPLY":
                return left * right

            elif node.operator.type == "DIVIDE":
                return left / right