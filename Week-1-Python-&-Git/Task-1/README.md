# Task 1 - Python & Git Basics

**Name:** Hammad Ali  
**Cohort:** GDGOC 2026  
**Fellowship:** AI/ML 2026

---

## 📌 Overview

This task demonstrates fundamental Python programming skills and Git version control basics. It includes core programming exercises covering mathematical calculations, string manipulation, control flow, and conceptual understanding of AI/ML/DL/DS.

---

## 📂 Files

### 1. `reading_summary.md` - AI/ML/DL/DS Overview

**Purpose:** Concise summary explaining the differences between Artificial Intelligence, Machine Learning, Deep Learning, and Data Science.

**Content:**
- Clear definitions of each field
- Relationships and hierarchies
- Practical applications
- Key distinctions

**View:**
```bash
cat reading_summary.md
```

---

### 2. `area_of_circle.py` - Circle Area Calculator

**Purpose:** Calculate the area of a circle given its radius using the mathematical formula: Area = π × r²

**Features:**
- ✅ Mathematical calculation using `math.pi`
- ✅ User input validation
- ✅ Error handling for invalid inputs
- ✅ Formatted output with 2 decimal places

**Run:**
```bash
python area_of_circle.py
```

**Example:**
```
Enter the radius of the circle: 5
The area of the circle with radius 5.0 is: 78.54
```

---

### 3. `factorial.py` - Factorial Calculator

**Purpose:** Calculate the factorial of a non-negative integer using iterative approach.

**Features:**
- ✅ Iterative factorial calculation (n! = n × (n-1) × ... × 1)
- ✅ Handles edge cases (0! = 1, 1! = 1)
- ✅ Input validation for negative numbers
- ✅ Error handling for non-integer inputs

**Run:**
```bash
python factorial.py
```

**Example:**
```
Enter a non-negative integer to calculate its factorial: 5
The factorial of 5 is 120
```

**Algorithm:**
```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

---

### 4. `String_reverse.py` - String Reversal

**Purpose:** Reverse a string using Python's slicing notation.

**Features:**
- ✅ String slicing (`[::-1]`)
- ✅ User input handling
- ✅ Displays both original and reversed strings

**Run:**
```bash
python String_reverse.py
```

**Example:**
```
Enter a string to reverse: Hello World
Original: Hello World
Reversed: dlroW olleH
```

**Method:** Uses Python's elegant slicing syntax `s[::-1]` to reverse the string.

---

### 5. `number_guessing_game.py` - Number Guessing Game

**Purpose:** Interactive game where the user guesses a randomly generated number between 1 and 100.

**Features:**
- ✅ Random number generation using `random.randint()`
- ✅ Interactive user feedback (Too high/Too low)
- ✅ Attempt counter
- ✅ Input validation
- ✅ Loop until correct guess

**Run:**
```bash
python number_guessing_game.py
```

**Example:**
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 63
Congratulations! You guessed the number 63 in 3 attempts.
```

**Concepts Demonstrated:**
- Random number generation
- While loops
- Conditional statements
- Exception handling
- User interaction

---

## 🎯 Learning Outcomes

✔️ **Python Basics:** Variables, data types, operators  
✔️ **Control Flow:** If/else statements, while loops  
✔️ **Functions:** Built-in functions and imports  
✔️ **User Input:** Interactive programs with input validation  
✔️ **Error Handling:** Try/except blocks for robust code  
✔️ **Mathematical Operations:** Using Python's math module  
✔️ **String Manipulation:** Slicing and string operations  
✔️ **Random Module:** Generating random numbers  

---

## 🚀 Quick Start

Run all programs:
```bash
# View AI/ML/DL/DS summary
cat reading_summary.md

# Calculate area of circle
python area_of_circle.py

# Calculate factorial
python factorial.py

# Reverse a string
python String_reverse.py

# Play guessing game
python number_guessing_game.py
```

---

## 📝 Concepts Covered

### Python Fundamentals
- Variables and data types
- Arithmetic operations
- String operations
- Type conversion

### Control Structures
- If/elif/else statements
- While loops
- Loop control (break, continue)

### Functions & Modules
- Importing modules (`math`, `random`)
- Using built-in functions
- Input/output operations

### Error Handling
- Try/except blocks
- ValueError handling
- Input validation

---

## 📚 Key Takeaways

1. **Mathematical Precision:** Using `math.pi` for accurate calculations
2. **Input Validation:** Always validate user inputs to prevent errors
3. **User Experience:** Provide clear prompts and feedback
4. **Code Organization:** Clean, readable code with proper formatting
5. **Error Handling:** Graceful handling of invalid inputs

---

**Completion Date:** January 28, 2026  
**Status:** ✅ Completed
