from node import NumberNode, IdentifierNode, BinaryOperationNode


class SemanticAnalyzer:

    def __init__(self):
        # Predefined variables
        self.symbol_table = {
            "a": 10,
            "b": 20,
            "c": 30
        }

    def analyze(self, node):

        if isinstance(node, NumberNode):
            return

        elif isinstance(node, IdentifierNode):

            if node.name not in self.symbol_table:
                raise Exception(
                    f"Semantic Error: Variable '{node.name}' is not defined."
                )

        elif isinstance(node, BinaryOperationNode):

            self.analyze(node.left)
            self.analyze(node.right)

            # Check Division by Zero
            if node.operator.type == "DIVIDE":

                if isinstance(node.right, NumberNode):

                    if node.right.value == 0:
                        raise Exception(
                            "Semantic Error: Division by zero."
                        )