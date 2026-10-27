class Node:
    """
    Base class for all AST nodes.
    """
    pass


class NumberNode(Node):
    def __init__(self, token):
        self.token = token
        self.value = token.value

    def __str__(self):
        return str(self.value)


class IdentifierNode(Node):
    def __init__(self, token):
        self.token = token
        self.name = token.value

    def __str__(self):
        return self.name


class BinaryOperationNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"({self.left} {self.operator.value} {self.right})"