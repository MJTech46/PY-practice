# Python Type Annotations

Type annotations in Python allow developers to specify the types of variables, function parameters, and return values. While Python is dynamically typed by nature, type hints are a way to indicate what types are expected, which helps improve code readability and can be useful for static analysis tools.

## What are Type Annotations?

Type annotations are a way of specifying the expected types of variables and function arguments in Python. They are not enforced by Python at runtime, but can be checked using external tools such as `mypy`.

## Benefits of Type Annotations

- **Improved Code Readability**: Type annotations provide a clear understanding of the types expected for variables and function arguments, making the code easier to follow.
- **Error Detection**: Static type checkers, like `mypy`, can catch type-related errors before running the program, reducing runtime issues.
- **IDE Support**: Many IDEs use type annotations to offer better code completion, refactoring support, and inline documentation.
- **Documentation**: Type hints serve as self-explanatory documentation, helping developers understand the function and variable types without additional comments.

## Using `mypy` for Type Checking

Type hints are not enforced at runtime, but you can use static type checkers like `mypy` to verify that your code adheres to the specified types.

### Installation

To install `mypy`, use `pip`:

```bash
pip install mypy
```

Once installed, you can run mypy on your Python scripts to check for type inconsistencies:

```bash
mypy your_script.py
```

If there are any type mismatches in your code, mypy will flag them, allowing you to correct errors before running the program.
