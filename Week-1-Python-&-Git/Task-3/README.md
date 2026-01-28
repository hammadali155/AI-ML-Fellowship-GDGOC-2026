# Task 3 - Object-Oriented & Advanced Python

**Name:** Hammad Ali  
**Cohort:** GDGOC 2026  
**Fellowship:** AI/ML 2026

---

## 📌 Overview

This task demonstrates mastery of advanced Python programming concepts including Object-Oriented Programming (OOP), decorators, generators, and iterators. The code showcases professional software development patterns and Python internals.

**Topics Covered:**
- **OOP Concepts:** Classes, Objects, Encapsulation, Inheritance, Polymorphism
- **Magic Methods:** `__init__`, `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`, `__sub__`
- **Decorators:** Function wrappers, decorator factories, memoization
- **Generators & Iterators:** Memory-efficient iteration, lazy evaluation

---

## 📂 Files

### 1. `bank_account.py` - Bank Account System (OOP)

**Purpose:** Comprehensive banking system demonstrating all OOP principles

**Class Hierarchy:**
```
BankAccount (Base)
    ├── SavingsAccount
    │       └── PremiumAccount (Multi-level)
    └── CheckingAccount
```

---

#### `BankAccount` (Base Class)

**Encapsulation:**
- Private attributes: `__account_holder`, `__account_number`, `__balance`, `__transaction_history`
- Public getters: `get_account_holder()`, `get_account_number()`, `get_balance()`

**Features:**
- ✅ Deposit money with validation
- ✅ Withdraw money with balance check
- ✅ Transaction history tracking
- ✅ Account information display
- ✅ Class variable tracking (total accounts)

**Magic Methods:**
```python
__str__()    # User-friendly string representation
__repr__()   # Developer representation
__eq__()     # Equality comparison by account number
__lt__()     # Less-than comparison by balance
__add__()    # Deposit using + operator
__sub__()    # Withdraw using - operator
```

**Example Usage:**
```python
acc = BankAccount("Hammad Ali", "ACC001", 1000)
acc.deposit(500)        # Traditional method
acc + 100               # Using + operator (magic method)
acc - 50                # Using - operator (magic method)
print(acc)              # Calls __str__()
```

---

#### `SavingsAccount` (Inherits from BankAccount)

**Inheritance Features:**
- Extends `BankAccount` with interest functionality
- Overrides `display_info()` to show interest rate
- Custom `__str__()` representation

**Additional Features:**
- ✅ Interest rate management
- ✅ `apply_interest()` method
- ✅ Default 3% interest rate

**Example:**
```python
savings = SavingsAccount("Sara Khan", "SAV001", 5000, 0.04)
savings.apply_interest()  # Adds 4% interest to balance
```

---

#### `CheckingAccount` (Inherits from BankAccount)

**Polymorphism:**
- Overrides `withdraw()` method for overdraft protection
- Different behavior than parent class

**Additional Features:**
- ✅ Overdraft limit (default $500)
- ✅ Allows negative balance up to limit
- ✅ Overdraft warning messages

**Example:**
```python
checking = CheckingAccount("Ahmed", "CHK001", 1000, 500)
checking.withdraw(1200)  # Uses overdraft (balance becomes -$200)
```

---

#### `PremiumAccount` (Multi-level Inheritance)

**Extends:** `SavingsAccount` → `BankAccount`

**Additional Features:**
- ✅ Higher interest rate (5%)
- ✅ Reward points system (1 point per $10 deposited)
- ✅ Points redemption (100 points = $1)
- ✅ Overridden `deposit()` to earn points

**Example:**
```python
premium = PremiumAccount("Hammad Ali", "PREM001", 10000)
premium.deposit(500)        # Earns 50 reward points
premium.redeem_points(100)  # Converts 100 points to $1
```

---

**Run:**
```bash
python bank_account.py
```

**Demonstration Output:**
- Account creation and management
- Deposit/withdrawal operations
- Interest calculation
- Overdraft handling
- Reward points system
- Transaction history
- Magic method usage

---

### 2. `decorators.py` - Function Decorators

**Purpose:** Custom decorators for function enhancement and monitoring

---

#### `@execution_time`
Measures and displays function execution time

```python
@execution_time
def slow_function():
    time.sleep(1)
    return "Done"
```

**Output:** `Function 'slow_function' executed in 1.000532 seconds`

---

#### `@timer_with_message(message)`
Decorator factory with custom message

```python
@timer_with_message("Matrix multiplication completed")
def matrix_multiply(size):
    # Matrix operations
    return result
```

---

#### `@debug`
Prints function signature and return value

```python
@debug
def add_numbers(a, b):
    return a + b

# Output:
# Calling add_numbers(5, 7)
# add_numbers() returned 12
```

---

#### `@memoize`
Caches function results for performance

```python
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# First call: calculates
# Second call: returns cached result
```

---

#### `@repeat(times)`
Repeats function execution N times

```python
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Executes greet() 3 times
```

---

#### `@validate_types(**type_hints)`
Validates argument types at runtime

```python
@validate_types(name=str, age=int)
def create_profile(name, age):
    return {"name": name, "age": age}

create_profile("Hammad", "twenty")  # Raises TypeError
```

---

#### `@rate_limit(max_calls, time_window)`
Limits function call rate

```python
@rate_limit(max_calls=3, time_window=5)
def api_call(endpoint):
    return {"status": "success"}

# Allows only 3 calls per 5 seconds
```

---

**Decorator Stacking:**
```python
@execution_time
@memoize
def expensive_operation(n):
    time.sleep(0.5)
    return n ** 2
```

**Run:**
```bash
python decorators.py
```

---

### 3. `generators.py` - Generators & Iterators

**Purpose:** Memory-efficient iteration using generators and custom iterators

---

#### Core Generators

**`fibonacci_generator(limit=None)`**
- Generates Fibonacci sequence
- Can be infinite (limit=None) or finite

```python
for num in fibonacci_generator(10):
    print(num)  # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**`custom_range(start, stop=None, step=1)`**
- Custom implementation of Python's `range()`
- Supports positive and negative steps

```python
list(custom_range(0, 10, 2))  # [0, 2, 4, 6, 8]
list(custom_range(10))         # [0, 1, 2, ..., 9]
list(custom_range(10, 0, -1))  # [10, 9, 8, ..., 1]
```

**`prime_generator(limit=None)`**
- Generates prime numbers efficiently
- Supports infinite generation

**`factorial_generator(n)`**
- Yields (number, factorial) pairs
- From 0! to n!

**`chunk_generator(data, chunk_size)`**
- Splits data into chunks
- Memory-efficient for large datasets

**`infinite_counter(start=0, step=1)`**
- Demonstrates lazy evaluation
- Never-ending sequence

**`power_generator(base, max_power)`**
- Generates powers of a base number
- base⁰, base¹, base², ..., baseⁿ

---

#### Advanced Generators

**`filter_generator(iterable, condition)`**
- Custom filter using generators

**`map_generator(iterable, transform)`**
- Custom map using generators

**`alternating_generator(*iterables)`**
- Alternates between multiple iterables

---

#### Generator Expressions

```python
squares = (x**2 for x in range(10))
evens = (x for x in range(20) if x % 2 == 0)
```

---

#### Custom Iterator Class

```python
class CustomIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.max_value:
            raise StopIteration
        self.current += 1
        return self.current ** 2
```

---

**Memory Efficiency Demonstration:**
```python
list_comp = [x**2 for x in range(10000)]  # ~87KB
gen_exp = (x**2 for x in range(10000))    # ~200 bytes
# Memory saved: ~86.8KB
```

**Run:**
```bash
python generators.py
```

---

## 🎯 Learning Outcomes

✔️ **OOP Mastery:** Classes, inheritance, polymorphism, encapsulation  
✔️ **Magic Methods:** Operator overloading, custom object behavior  
✔️ **Decorators:** Function modification, memoization, validation  
✔️ **Generators:** Memory-efficient iteration, lazy evaluation  
✔️ **Python Internals:** Deep understanding of Python mechanisms  
✔️ **Design Patterns:** Professional software architecture  

---

## 📊 Concepts Comparison

### Lists vs Generators

| Feature | List | Generator |
|---------|------|-----------|
| Memory | Stores all items in memory | Generates items on-the-fly |
| Speed | Fast random access | Slower per item, but efficient overall |
| Use Case | Small datasets | Large/infinite datasets |
| Creation | `[x**2 for x in range(1000)]` | `(x**2 for x in range(1000))` |
| Iteration | Can iterate multiple times | Single iteration (exhausted after use) |

### Inheritance Types

| Type | Example | Description |
|------|---------|-------------|
| Single | `SavingsAccount` → `BankAccount` | One parent class |
| Multi-level | `PremiumAccount` → `SavingsAccount` → `BankAccount` | Chain of inheritance |

---

## 🚀 Quick Start

```bash
# Bank account system demonstration
python bank_account.py

# Decorator examples
python decorators.py

# Generator demonstrations
python generators.py
```

---

## 🔍 Advanced Concepts

### Encapsulation
- **Private attributes:** `__balance` (name mangling)
- **Public getters:** Controlled access to private data
- **Data hiding:** Protection from external modification

### Inheritance
- **Code reuse:** Child classes inherit parent methods
- **Extension:** Add new features to inherited classes
- **`super()`:** Access parent class methods

### Polymorphism
- **Method overriding:** `withdraw()` in `CheckingAccount`
- **Same interface, different behavior**
- **Runtime method resolution**

### Magic Methods
```python
__init__(self, ...)      # Constructor
__str__(self)            # str(obj), print(obj)
__repr__(self)           # repr(obj), debugging
__eq__(self, other)      # obj1 == obj2
__lt__(self, other)      # obj1 < obj2
__add__(self, other)     # obj + value
__sub__(self, other)     # obj - value
```

### Decorator Patterns
- **Simple decorator:** Wraps a function
- **Decorator factory:** Returns a decorator (parameterized)
- **`@functools.wraps`:** Preserves function metadata
- **Decorator stacking:** Multiple decorators on one function

### Generator Benefits
- **Memory efficient:** Don't store entire sequence
- **Lazy evaluation:** Compute values on demand
- **Infinite sequences:** Can represent unbounded data
- **`yield` keyword:** Suspends function state

---

## 📚 Resources

- **OOP Guide:** [Real Python - OOP](https://realpython.com/python3-object-oriented-programming/)
- **Decorators:** [Real Python - Decorators](https://realpython.com/primer-on-python-decorators/)
- **Generators:** [Real Python - Generators](https://realpython.com/introduction-to-python-generators/)

---

**Submission Date:** January 28, 2026  
**Status:** ✅ Completed
