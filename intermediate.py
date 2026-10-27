from node import NumberNode, IdentifierNode, BinaryOperationNode


class IntermediateCodeGenerator:

    def __init__(self):
        self.temp_count = 1
        self.code = []

    def new_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def generate(self, node):

        # Number
        if isinstance(node, NumberNode):
            return str(node.value)

        # Variable
        elif isinstance(node, IdentifierNode):
            return node.name

        # Binary Operation
        elif isinstance(node, BinaryOperationNode):

            left = self.generate(node.left)
            right = self.generate(node.right)

            temp = self.new_temp()

            instruction = f"{temp} = {left} {node.operator.value} {right}"

            self.code.append(instruction)

            return temp