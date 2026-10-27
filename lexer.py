from mytoken import Token


class Lexer:

    def __init__(self, text):
        self.text = text
        self.position = 0

    # Return current character
    def current_char(self):
        if self.position >= len(self.text):
            return None
        return self.text[self.position]

    # Move to next character
    def advance(self):
        self.position += 1

    # Read a complete number
    def number(self):
        result = ""

        while self.current_char() is not None and self.current_char().isdigit():
            result += self.current_char()
            self.advance()

        return Token("NUMBER", int(result))

    # Read an identifier (variable names)
    def identifier(self):
        result = ""

        while self.current_char() is not None and self.current_char().isalpha():
            result += self.current_char()
            self.advance()

        return Token("IDENTIFIER", result)

    # Main function
    def tokenize(self):

        tokens = []

        while self.current_char() is not None:

            char = self.current_char()

            # Ignore spaces
            if char.isspace():
                self.advance()

            # Numbers
            elif char.isdigit():
                tokens.append(self.number())

            # Variables
            elif char.isalpha():
                tokens.append(self.identifier())

            # Operators
            elif char == '+':
                tokens.append(Token("PLUS", '+'))
                self.advance()

            elif char == '-':
                tokens.append(Token("MINUS", '-'))
                self.advance()

            elif char == '*':
                tokens.append(Token("MULTIPLY", '*'))
                self.advance()

            elif char == '/':
                tokens.append(Token("DIVIDE", '/'))
                self.advance()

            elif char == '(':
                tokens.append(Token("LEFT_PAREN", '('))
                self.advance()

            elif char == ')':
                tokens.append(Token("RIGHT_PAREN", ')'))
                self.advance()

            else:
                raise Exception(f"Invalid Character : {char}")

        return tokens