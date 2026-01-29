# Task 4: Libraries, Packaging & Documentation

This task focuses on understanding **modularity**, **packaging**, and **production readiness** in Python. I have organized the code into modules and a custom package to demonstrate cleaner code structure.

## Structure

### 1. `modules/`
Contains standalone utility modules.
- `math_module.py`: Basic math operations and statistics (Sum, Max, Min, Avg).
- `string_module.py`: String processing functions.

### 2. `mypackage/`
A custom Python package example.
- `__init__.py`: Package initialization.
- `calculator.py`: Contains `SimpleCalculator` class.

### 3. `main.py`
The entry point script that imports and demonstrates usage of both the modules and the custom package.

### 4. `requirements.txt`
Lists project dependencies (currently empty as we use standard libraries).

## How to Run

1. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   ```

2. **Activate Virtual Environment:**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Main Script:**
   ```bash
   python main.py
   ```

