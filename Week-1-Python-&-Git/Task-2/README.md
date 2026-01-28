# Task 2 - Modular Python, Data Handling, File Handling & Exceptions

**Name:** Hammad Ali  
**Cohort:** GDGOC 2026  
**Fellowship:** AI/ML 2026

---

## 📌 Overview

This task demonstrates proficiency in advanced Python concepts including:
- Advanced function usage (`*args`, `**kwargs`, lambda functions)
- File handling (read/write/append operations)
- Exception handling (`try/except/else/finally`)
- Built-in data structures (lists, dictionaries, sets, tuples)
- List and dictionary comprehensions
- Time and space complexity awareness

---

## 📂 Files

### 1. `utils.py` - Utility Functions Module
**Purpose:** Demonstrates advanced function usage with `*args`, `**kwargs`, and lambda functions

**Features:**
- ✅ Functions with variable arguments (`*args`)
- ✅ Functions with keyword arguments (`**kwargs`)
- ✅ Lambda function examples (square, add, is_even, get_max)
- ✅ Higher-order functions (apply_operation, filter_data)
- ✅ Statistical calculations using `*args`
- ✅ Profile building with mixed arguments

**Run:**
```bash
python utils.py
```

---

### 2. `contact_manager.py` - File-Based Contact Manager
**Purpose:** Store and manage contacts using file operations (JSON-based)

**Features:**
- ✅ Add, update, delete contacts
- ✅ Search and view all contacts
- ✅ Persistent storage using JSON file
- ✅ Safe file handling with error checking
- ✅ Interactive menu system

**Run:**
```bash
python contact_manager.py
```

**Data Storage:** Creates `contacts.json` file for persistent storage

---

### 3. `exception_handling.py` - Exception-Safe Calculator
**Purpose:** Demonstrate comprehensive exception handling

**Features:**
- ✅ Handle `ZeroDivisionError`, `ValueError`, `TypeError`
- ✅ Complete `try/except/else/finally` blocks
- ✅ Interactive calculator with calculation history
- ✅ Multiple exception type demonstrations
- ✅ Safe numeric input validation

**Run:**
```bash
python exception_handling.py
```

---

### 4. `student_records.py` - Student Record System
**Purpose:** Manage student records using dictionaries and lists

**Features:**
- ✅ Add, update, delete student records
- ✅ Dictionary-based student data with nested grade information
- ✅ Calculate average grades automatically
- ✅ Display all students in formatted table
- ✅ Search by roll number
- ✅ Get top N students by average
- ✅ Overall statistics (class average, highest/lowest)
- ✅ Filter students by minimum average

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

**Run:**
```bash
python student_records.py
```

---

### 5. `data_op.py` - Data Manipulation (Optional)
**Purpose:** Advanced data manipulation with complexity analysis

**Features:**
- ✅ Remove duplicates (ordered & unordered)
- ✅ Sort data with custom key functions
- ✅ Find max/min/average/sum
- ✅ Merge sorted lists efficiently
- ✅ Find nth largest element
- ✅ Group data by property
- ✅ Frequency counting
- ✅ Find common elements
- ✅ Flatten nested lists
- ✅ List comprehensions (squares, filtering)
- ✅ Dictionary comprehensions
- ✅ Matrix transpose
- ⏱️ Time & space complexity annotations

**Run:**
```bash
python data_op.py
```

---

## 🎯 Learning Outcomes

✔️ **Modular Code:** Write reusable, well-organized functions  
✔️ **Data Structures:** Confident use of lists, dictionaries, sets, tuples  
✔️ **File Operations:** Safe read/write/append operations  
✔️ **Error Handling:** Real-world exception handling  
✔️ **Comprehensions:** Efficient list/dict comprehensions  
✔️ **Algorithm Awareness:** Basic understanding of time/space complexity  

---

## 🚀 Quick Start

Run all demonstrations:
```bash
# Utility functions demo
python utils.py

# Contact manager (interactive)
python contact_manager.py

# Exception handling demo
python exception_handling.py

# Student records system
python student_records.py

# Data manipulation operations
python data_op.py
```

---

## 📊 Complexity Analysis Examples

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Remove duplicates (ordered) | O(n) | O(n) |
| Sort data | O(n log n) | O(n) |
| Find statistics | O(n) | O(1) |
| Merge sorted lists | O(n + m) | O(n + m) |
| Frequency count | O(n) | O(n) |

---

## 📝 Notes

- All files include comprehensive error handling
- Code follows PEP 8 style guidelines
- Extensive inline documentation
- Interactive demonstrations included
- Sample data provided for testing

---

**Submission Date:** January 27, 2026  
**Repository:** [GitHub Link]
