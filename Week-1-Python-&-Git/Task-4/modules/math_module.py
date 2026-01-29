def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def calculate_stats(numbers):
    if not numbers:
        return None
    return {
        "sum": sum(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers)
    }