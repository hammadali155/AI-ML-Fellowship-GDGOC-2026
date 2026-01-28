# Task 2 - Modular Python, Data Handling, File Handling & Exceptions

**Name:** Hammad Ali  
**Cohort:** GDGOC 2026  
**Fellowship:** AI/ML 2026

---

## 📌 Overview

This task demonstrates proficiency in advanced Python concepts including modular programming, data structure manipulation, file I/O operations, and comprehensive exception handling. The focus is on writing clean, reusable, and production-ready code.

**Topics Covered:**
- Advanced function usage (`*args`, `**kwargs`)
- Lambda functions
- File handling (Read/Write/Append)
- Exception handling (`try/except/else/finally`)
- Data structures (Lists, Dictionaries, Sets, Tuples)
- List and Dictionary comprehensions
- Algorithm complexity awareness

---

## 📂 Files

### 1. `utils.py` - Utility Functions Module

**Purpose:** Reusable utility functions demonstrating advanced Python features

**Functions:**

#### `greet(*args)`
- Greets multiple people using variable arguments
- Returns formatted greeting string

#### `describe_person(**kwargs)`
- Describes a person using keyword arguments
- Returns formatted description

#### Lambda Functions
```python
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0
get_max = lambda *args: max(args) if args else None
```

#### `apply_operation(numbers, operation)`
- Applies a lambda operation to a list of numbers
- Returns list of results

#### `filter_data(data, condition)`
- Filters data based on a lambda condition
- Returns filtered list

#### `calculate_statistics(*numbers)`
- Calculates sum, average, min, max, and count
- Returns dictionary with statistics

**Run:**
```bash
python utils.py
```

---

### 2. `contact_manager.py` - File-Based Contact Manager

**Purpose:** Persistent contact storage using JSON file handling

**Features:**
- ✅ Add new contacts (name, phone, email)
- ✅ Update existing contacts
- ✅ Delete contacts with confirmation
- ✅ View all contacts in formatted table
- ✅ Search for specific contacts
- ✅ JSON file storage (`contacts.json`)
- ✅ Safe file operations with error handling

**Functions:**
- `load_contacts()` - Load from JSON file
- `save_contacts(contacts)` - Save to JSON file
- `add_contact(name, phone, email)` - Add new contact
- `update_contact(name, phone, email)` - Update existing
- `delete_contact(name)` - Remove contact
- `view_contacts()` - Display all contacts
- `search_contact(name)` - Find specific contact

**Run:**
```bash
python contact_manager.py
```

**Data Storage:** Creates `contacts.json` in the same directory

---

### 3. `exception_handling.py` - Exception-Safe Calculator

**Purpose:** Interactive calculator with comprehensive error handling

**Features:**
- ✅ Basic operations (+, -, *, /)
- ✅ Calculation history
- ✅ Multiple exception types handled:
  - `ZeroDivisionError`
  - `ValueError`
  - `TypeError`
  - `KeyboardInterrupt`
- ✅ `try/except/else/finally` blocks
- ✅ Safe numeric input validation

**Functions:**
- `safe_divide(a, b)` - Division with error handling
- `get_numeric_input(prompt)` - Validated number input
- `calculate(num1, num2, operation)` - Perform calculation
- `advanced_calculator()` - Interactive calculator with history

**Run:**
```bash
python exception_handling.py
```

**Exception Handling Pattern:**
```python
try:
    # Risky operation
    result = a / b
except ZeroDivisionError:
    # Handle specific error
    print("Error: Division by zero!")
except ValueError:
    # Handle another error
    print("Error: Invalid value!")
else:
    # Executes if no exception
    print("Success!")
finally:
    # Always executes
    print("Cleanup complete")
```

---

### 4. `student_records.py` - Student Record System

**Purpose:** Manage student records using dictionaries and lists

**Data Structure:**
```python
student = {
    'roll_no': int,
    'name': str,
    'age': int,
    'grades': {'subject': grade},
    'average': float
}
```

**Features:**
- ✅ Add students with multiple subjects
- ✅ Update student information
- ✅ Delete students
- ✅ Display all students in formatted table
- ✅ Search by roll number
- ✅ Get top N students by average
- ✅ Calculate class statistics
- ✅ Filter students by minimum average
- ✅ Automatic average calculation

**Functions:**
- `add_student(roll_no, name, age, grades)` - Add new student
- `update_student(roll_no, **kwargs)` - Update student data
- `delete_student(roll_no)` - Remove student
- `display_all_students()` - Show all records
- `search_student(roll_no)` - Find student
- `get_top_students(n)` - Get top performers
- `get_statistics()` - Class statistics
- `filter_students_by_average(min_average)` - Filter by grade

**Run:**
```bash
python student_records.py
```

**Sample Data Included:**
- Hammad Ali (Roll: 101)
- Haris Khan (Roll: 102)
- Shahid Zahoor (Roll: 103)

---

### 5. `data_op.py` - Data Manipulation (Optional)

**Purpose:** Advanced data operations with complexity analysis

**Operations:**

#### List Operations
- `remove_duplicates_list(data)` - O(n) time, O(n) space
- `remove_duplicates_set(data)` - O(n) time, O(n) space
- `sort_data(data, reverse, key)` - O(n log n) time
- `merge_sorted_lists(list1, list2)` - O(n + m) time

#### Statistical Operations
- `find_statistics(numbers)` - O(n) time, O(1) space
- `find_nth_largest(numbers, n)` - O(n log n) time
- `frequency_count(data)` - O(n) time, O(n) space

#### Set Operations
- `find_common_elements(list1, list2)` - O(n + m) time
- `group_by_property(data, key_func)` - O(n) time

#### List Comprehensions
- `squares_of_evens(numbers)` - Filter and transform
- `filter_by_length(strings, min_length)` - Filter strings
- `transpose_matrix(matrix)` - Nested comprehensions

**Run:**
```bash
python data_op.py
```

---

## 🎯 Learning Outcomes

✔️ **Modular Code:** Write reusable, well-organized functions  
✔️ **Data Structures:** Master lists, dictionaries, sets, tuples  
✔️ **File Operations:** Safe read/write/append operations  
✔️ **Error Handling:** Production-ready exception handling  
✔️ **Comprehensions:** Efficient list/dict comprehensions  
✔️ **Algorithm Awareness:** Understand time/space complexity  

---

## 🚀 Quick Start

```bash
# Utility functions demo
python utils.py

# Contact manager (interactive)
python contact_manager.py

# Exception-safe calculator
python exception_handling.py

# Student records system
python student_records.py

# Data manipulation operations
python data_op.py
```

---

## 📊 Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Remove duplicates (ordered) | O(n) | O(n) |
| Sort data | O(n log n) | O(n) |
| Find statistics | O(n) | O(1) |
| Merge sorted lists | O(n + m) | O(n + m) |
| Frequency count | O(n) | O(n) |
| Find nth largest | O(n log n) | O(n) |

---

## 📝 Code Highlights

### Advanced Function Usage
```python
# *args example
def greet(*args):
    return f"Hello, {', '.join(args)}!"

# **kwargs example
def describe_person(**kwargs):
    return "\n".join([f"{k}: {v}" for k, v in kwargs.items()])
```

### Lambda Functions
```python
square = lambda x: x ** 2
is_even = lambda x: x % 2 == 0
```

### List Comprehensions
```python
squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
```

### Exception Handling
```python
try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result: {result}")
finally:
    print("Operation complete")
```

---

## 📚 Key Concepts

### File Handling
- Reading JSON files
- Writing JSON files
- Error handling for file operations
- Persistent data storage

### Data Structures
- Dictionaries for key-value storage
- Lists for ordered collections
- Sets for unique elements
- Tuples for immutable data

### Exception Types
- `ZeroDivisionError` - Division by zero
- `ValueError` - Invalid value
- `TypeError` - Wrong type
- `KeyError` - Missing dictionary key
- `IndexError` - Invalid list index
- `FileNotFoundError` - Missing file

---

**Submission Date:** January 29, 2026  
**Status:** ✅ Completed
