from flask import Flask, render_template, request, jsonify
from lexer import Lexer
from parser import Parser
from semantic import SemanticAnalyzer
from intermediate import IntermediateCodeGenerator
from evaluator import Evaluator

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False


def ast_to_dict(node):
    """Convert the existing AST nodes to a JSON-friendly tree."""
    from node import NumberNode, IdentifierNode, BinaryOperationNode
    if isinstance(node, NumberNode):
        return {"type": "Number", "value": node.value}
    if isinstance(node, IdentifierNode):
        return {"type": "Variable", "name": node.name}
    if isinstance(node, BinaryOperationNode):
        return {
            "type": "Operation",
            "operator": node.operator.value,
            "left": ast_to_dict(node.left),
            "right": ast_to_dict(node.right),
        }
    return {"type": "Unknown"}


def compile_expression(expression):
    if not expression or not expression.strip():
        raise ValueError("Please enter an arithmetic expression.")

    # 1. Lexical analysis
    tokens = Lexer(expression).tokenize()
    if not tokens:
        raise ValueError("Please enter an arithmetic expression.")

    # 2. Syntax analysis / AST
    parser = Parser(tokens)
    tree = parser.parse()
    # The current Parser.parse() doesn't check for leftover tokens (e.g. '2 3').
    if parser.current_token() is not None:
        raise ValueError(f"Unexpected token: {parser.current_token().value}")

    # 3. Semantic analysis
    semantic = SemanticAnalyzer()
    semantic.analyze(tree)

    # 4. Intermediate code generation
    generator = IntermediateCodeGenerator()
    generator.generate(tree)

    # 5. Evaluation
    evaluator = Evaluator()
    try:
        result = evaluator.evaluate(tree)
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed.")

    return {
        "expression": expression,
        "tokens": [{"type": token.type, "value": str(token.value)} for token in tokens],
        "ast_text": str(tree),
        "ast": ast_to_dict(tree),
        "semantic": "Passed",
        "intermediate_code": generator.code,
        "result": result,
        "variables": semantic.symbol_table,
    }


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/compile")
def compile_route():
    data = request.get_json(silent=True) or request.form
    expression = data.get("expression", "")
    try:
        return jsonify({"success": True, "data": compile_expression(expression)})
    except Exception as exc:
        return jsonify({"success": False, "error": str(exc)}), 400


if __name__ == "__main__":
    app.run(debug=True)
