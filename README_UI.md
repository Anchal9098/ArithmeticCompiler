# Arithmetic Compiler — Ready-to-Run Web UI

## Windows: easiest way
1. Extract the entire `ArithmeticCompiler_Ready` folder from the ZIP.
2. Install Python 3.10 or newer if it is not installed. During installation, enable **Add Python to PATH**.
3. Double-click **`run.bat`**.
4. The first run creates a local `.venv` folder and installs Flask. An internet connection is needed for this first setup.
5. The app opens in your browser at **http://127.0.0.1:5000**. Keep the black terminal window open while using it.
6. To stop the server, focus the terminal window and press **Ctrl+C**.

## Manual launch
From this folder in a terminal:
```bash
python -m pip install -r requirements.txt
python app.py
```
Then visit http://127.0.0.1:5000.

## What's included
- `app.py`: Flask web server that connects the UI to your compiler modules.
- `templates/index.html` and `static/style.css`: user interface.
- `lexer.py`, `parser.py`, `node.py`, `mytoken.py`, `semantic.py`, `intermediate.py`, `evaluator.py`: compiler logic.
- `main.py`: original terminal-based entry point; the web UI uses `app.py` instead.

## Supported expression syntax
Integer numbers, alphabetic variables `a`, `b`, `c`, operators `+ - * /`, and parentheses. Predefined values are `a = 10`, `b = 20`, `c = 30`.

Examples: `5 + 3`, `5 + 3 * 2`, `(5 + 6) * 7`, `a + b * 2`.

This app runs locally on your computer; it is not published on the internet.
