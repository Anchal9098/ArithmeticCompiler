from node import NumberNode, IdentifierNode, BinaryOperationNode


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    # Return current token
    def current_token(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]

    # Move to next token
    def advance(self):
        self.position += 1

    # -----------------------------
    # Factor
    # NUMBER
    # IDENTIFIER
    # ( Expression )
    # -----------------------------
    def factor(self):

        token = self.current_token()

        if token.type == "NUMBER":
            self.advance()
            return NumberNode(token)

        elif token.type == "IDENTIFIER":
            self.advance()
            return IdentifierNode(token)

        elif token.type == "LEFT_PAREN":

            self.advance()

            node = self.expression()

            if self.current_token().type != "RIGHT_PAREN":
                raise Exception("Missing ')' ")

            self.advance()

            return node

        else:
            raise Exception("Invalid Syntax")

    # -----------------------------
    # Term
    # *, /
    # -----------------------------
    def term(self):

        node = self.factor()

        while self.current_token() is not None and \
              self.current_token().type in ("MULTIPLY", "DIVIDE"):

            operator = self.current_token()

            self.advance()

            right = self.factor()

            node = BinaryOperationNode(node, operator, right)

        return node

    # -----------------------------
    # Expression
    # +,-
    # -----------------------------
    def expression(self):

        node = self.term()

        while self.current_token() is not None and \
              self.current_token().type in ("PLUS", "MINUS"):

            operator = self.current_token()

            self.advance()

            right = self.term()

            node = BinaryOperationNode(node, operator, right)

        return node

    # Start parsing
    def parse(self):
        return self.expression()