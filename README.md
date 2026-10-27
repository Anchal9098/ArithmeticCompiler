# Arithmetic Expression Compiler

## Project Overview

This project is a mini compiler developed in Python for arithmetic expressions. It demonstrates the basic phases of compiler construction, including lexical analysis, syntax analysis, semantic analysis, intermediate code generation, and expression evaluation.

The compiler accepts arithmetic expressions containing numbers, variables, operators, and parentheses.

Example:

```
(5+6)*7
```

---

## Features

- Lexical Analysis (Token Generation)
- Syntax Analysis (Parser)
- Abstract Syntax Tree (AST)
- Semantic Analysis
- Three Address Code Generation
- Expression Evaluation

---

## Supported Operators

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

---

## Supported Inputs

Examples:

```
5+3

10*20

(5+6)*7

a+b*2
```

---

## Project Structure

```
ArithmeticCompiler/
│
├── main.py
├── mytoken.py
├── lexer.py
├── parser.py
├── node.py
├── semantic.py
├── intermediate.py
├── evaluator.py
└── README.md
```

---

## Compiler Phases

### 1. Lexical Analysis

Converts the input expression into tokens.

Example

Input

```
5+3
```

Output

```
NUMBER : 5
PLUS : +
NUMBER : 3
```

---

### 2. Syntax Analysis

Checks whether the expression follows the grammar rules and builds an Abstract Syntax Tree.

---

### 3. Semantic Analysis

Checks for semantic errors like

- Undefined Variables
- Division by Zero

---

### 4. Intermediate Code Generation

Generates Three Address Code.

Example

Input

```
5+3*2
```

Output

```
t1 = 3 * 2
t2 = 5 + t1
```

---

### 5. Evaluation

Evaluates the expression and produces the final result.

Example

```
5+3*2
```

Output

```
11
```

---

## Requirements

- Python 3.x
- Visual Studio Code (Recommended)

---

## How to Run

Open terminal inside the project folder.

Run

```
python main.py
```

Enter an arithmetic expression.

Example

```
Enter Expression:
(5+6)*7
```

Output

- Tokens
- AST
- Semantic Analysis
- Three Address Code
- Final Result

---

## Future Improvements

- Floating point numbers
- Unary operators
- Exponent operator (^)
- Variable assignment
- Better error handling
- GUI using Tkinter