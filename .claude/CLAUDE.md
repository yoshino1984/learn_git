# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: Python Learning Example

A simple Python learning project demonstrating basic Python programming concepts including modular programming, function definitions, docstrings, conditional logic, and exception handling.

## Common Commands

### Run the main program
```bash
python main.py
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Code Structure

- `main.py` - Main program entry point with `hello_world()` and `main()` functions
- `utils.py` - Utility functions module containing:
  - `greet(name)` - Returns a greeting message
  - `calculate(a, b, operation)` - Calculator supporting add/subtract/multiply/divide operations
- `requirements.txt` - Project dependencies (currently empty)

## Code Style

- Follow PEP 8 conventions
- Use docstrings (`"""..."""`) for function documentation
- Shebang line: `#!/usr/bin/env python3`
- Use `if __name__ == "__main__":` guard for main execution
