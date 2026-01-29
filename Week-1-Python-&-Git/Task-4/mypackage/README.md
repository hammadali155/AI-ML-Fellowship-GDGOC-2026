# MyPackage Directory

This directory represents a custom Python package structure. It demonstrates how to organize code into reusable packages.

## Structure

- `__init__.py`: Makes this directory a Python package and exposes `SimpleCalculator`.
- `calculator.py`: Contains the implementation of the calculator class.

## Classes

### `SimpleCalculator`
Located in `calculator.py`.
- **Methods:**
  - `add_numbers(a, b)`: Adds two numbers.
  - `multiply_numbers(a, b)`: Multiplies two numbers.

## Usage
You can import the calculator directly from the package:
```python
from mypackage import SimpleCalculator
```
