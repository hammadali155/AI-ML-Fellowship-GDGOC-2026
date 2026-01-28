# Task 3 - Object-Oriented & Advanced Python

**Name:** Hammad Ali  
**Cohort:** GDGOC 2026  
**Fellowship:** AI/ML 2026

---

## 📌 Overview

This task demonstrates mastery of advanced Python concepts including:
- Object-Oriented Programming (OOP)
  - Classes and Objects
  - Encapsulation (private attributes, getters)
  - Inheritance (single and multi-level)
  - Polymorphism (method overriding)
  - Magic Methods (`__init__`, `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__sub__`)
- Decorators (function wrappers, decorator factories)
- Iterators and Generators (memory-efficient iteration)
- Advanced Python internals

---

## 📂 Files

### 1. `bank_account.py` - Bank Account System (OOP)

**Purpose:** Comprehensive demonstration of all OOP concepts

**Classes:**

#### `BankAccount` (Base Class)
- **Encapsulation:** Private attributes (`__balance`, `__account_holder`, `__account_number`)
- **Magic Methods:** `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__sub__`
- **Features:**
  - Deposit and withdraw with validation
  - Transaction history tracking
  - Account information display
  - Operator overloading (+ for deposit, - for withdraw)

#### `SavingsAccount` (Inherits from BankAccount)
- **Inheritance:** Extends BankAccount
- **Additional Features:**
  - Interest rate management
  - Apply interest to balance
  - Overridden display method

#### `CheckingAccount` (Inherits from BankAccount)
- **Polymorphism:** Overrides `withdraw()` method
- **Additional Features:**
  - Overdraft protection
  - Overdraft limit tracking
  - Modified withdrawal logic

#### `PremiumAccount` (Inherits from SavingsAccount)
- **Multi-level Inheritance:** Extends SavingsAccount
- **Additional Features:**
  - Higher interest rate (5%)
  - Reward points system
  - Points redemption
  - Overridden deposit method

**Run:**
```bash
python bank_account.py
```

**Sample Output:**
- Account creation and management
- Deposit/withdrawal operations
- Interest calculation
- Overdraft handling
- Reward points system
- Transaction history

---

### 2. `decorators.py` - Execution Time Decorator

**Purpose:** Custom decorators for various use cases

**Decorators:**

#### `@execution_time`
Measures and displays function execution time

#### `@timer_with_message(message)`
Decorator factory with custom completion message

#### `@debug`
Prints function signature and return value

#### `@memoize`
Caches function results for performance optimization

#### `@repeat(times)`
Repeats function execution N times

#### `@validate_types(**type_hints)`
Validates function argument types at runtime

#### `@rate_limit(max_calls, time_window)`
Limits function call rate

**Usage Example:**
```python
@execution_time
def my_function():
    # Function code
    pass

@timer_with_message("Processing completed")
@memoize
def expensive_operation(n):
    # Expensive computation
    pass
```

**Run:**
```bash
python decorators.py
```

**Features:**
- ✅ Execution timing with microsecond precision
- ✅ Function result caching (memoization)
- ✅ Type validation
- ✅ Rate limiting
- ✅ Decorator stacking (multiple decorators on one function)
- ✅ Decorator factories (parameterized decorators)

---

### 3. `generators.py` - Fibonacci & Custom Range Generators

**Purpose:** Demonstrate generators and iterators for memory-efficient operations

**Generators:**

#### `fibonacci_generator(limit=None)`
Generate Fibonacci sequence (finite or infinite)

#### `custom_range(start, stop=None, step=1)`
Custom implementation of Python's built-in `range()`

#### `prime_generator(limit=None)`
Generate prime numbers efficiently

#### `factorial_generator(n)`
Generate factorials from 0! to n!

#### `chunk_generator(data, chunk_size)`
Split data into chunks

#### `infinite_counter(start=0, step=1)`
Infinite counter (demonstrates lazy evaluation)

#### `alternating_generator(*iterables)`
Alternate between multiple iterables

#### `power_generator(base, max_power)`
Generate powers of a base number

#### `filter_generator(iterable, condition)`
Custom filter implementation using generators

#### `map_generator(iterable, transform)`
Custom map implementation using generators

**Custom Iterator:**
- `CustomIterator` class with `__iter__` and `__next__` methods

**Usage Example:**
```python
# Generate first 10 Fibonacci numbers
for num in fibonacci_generator(10):
    print(num)

# Custom range
for i in custom_range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Infinite counter (use with caution!)
counter = infinite_counter(start=1, step=1)
print(next(counter))  # 1
print(next(counter))  # 2
```

**Run:**
```bash
python generators.py
```

**Features:**
- ✅ Memory-efficient iteration
- ✅ Lazy evaluation
- ✅ Infinite sequences
- ✅ Generator expressions
- ✅ Custom iterator class
- ✅ Generator chaining
- ✅ Memory comparison (list vs generator)

---

## 🎯 Learning Outcomes

✔️ **OOP Mastery:** Deep understanding of classes, inheritance, polymorphism, and encapsulation  
✔️ **Magic Methods:** Operator overloading and custom object behavior  
✔️ **Decorators:** Function modification and enhancement  
✔️ **Generators:** Memory-efficient iteration and lazy evaluation  
✔️ **Python Internals:** Understanding how Python works under the hood  
✔️ **Design Patterns:** Proper software architecture using OOP principles  

---

## 📊 Concept Comparison

### Lists vs Generators

| Feature | List | Generator |
|---------|------|-----------|
| Memory | Stores all items | Generates on-the-fly |
| Speed | Fast access | Slower per item |
| Use Case | Small datasets | Large/infinite datasets |
| Example | `[x**2 for x in range(1000)]` | `(x**2 for x in range(1000))` |

### Inheritance Hierarchy

```
BankAccount (Base)
    ├── SavingsAccount
    │       └── PremiumAccount (Multi-level)
    └── CheckingAccount
```

---

## 🚀 Quick Start

Run all demonstrations:
```bash
# Bank account system
python bank_account.py

# Decorator examples
python decorators.py

# Generator demonstrations
python generators.py
```

---

## 🔍 Advanced Concepts Demonstrated

### Encapsulation
- Private attributes using double underscore (`__balance`)
- Public getters for controlled access
- Data hiding and protection

### Inheritance
- Single inheritance (SavingsAccount from BankAccount)
- Multi-level inheritance (PremiumAccount from SavingsAccount)
- Method inheritance and extension

### Polymorphism
- Method overriding (`withdraw()` in CheckingAccount)
- Different behaviors for same method call
- `super()` for parent class access

### Magic Methods
- `__init__`: Constructor
- `__str__`: User-friendly string representation
- `__repr__`: Developer-friendly representation
- `__eq__`: Equality comparison
- `__lt__`: Less-than comparison
- `__add__`: Addition operator
- `__sub__`: Subtraction operator

### Decorators
- Simple decorators
- Decorator factories (parameterized)
- Preserving metadata with `@functools.wraps`
- Decorator stacking

### Generators
- `yield` keyword
- Generator expressions
- Memory efficiency
- Lazy evaluation
- Infinite sequences

---

## 📚 Resources

- **OOP Guide:** [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- **Decorators:** [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)
- **Generators:** [Real Python - Generators](https://realpython.com/introduction-to-python-generators/)

---

**Submission Date:** January 28, 2026  
**Repository:** [GitHub Link]
