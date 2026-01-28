# multiple args module using args and kwargs

def greet(*args):
    if not args:
        return "Hello, nobody!"
    return f"Hello, {', '.join(args)}!"


def describe_person(**kwargs):
    if not kwargs:
        return "No information provided."
    
    description = []
    for key, value in kwargs.items():
        description.append(f"{key.capitalize()}: {value}")
    return "\n".join(description)




#lambda functions
square = lambda x: x ** 2
add = lambda x, y: x + y
is_even = lambda x: x % 2 == 0
get_max = lambda *args: max(args) if args else None




#some util modules
def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]


def filter_data(data, condition):
    return list(filter(condition, data))


def calculate_statistics(*numbers):
    if not numbers:
        return {"error": "No numbers provided"}
    
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers)
    }



if __name__ == "__main__":
    print("*args Demo")
    print(greet("Hammad", "Ali", "Khan"))
    
    print("\n**kwargs Demo")
    print(describe_person(name="Hammad Ali", cohort="GDGOC 2026", role="Fellow"))
    

    print("\nLambda Functions ")
    print(f"Square of 5: {square(5)}")
    print(f"Add 3 and 7: {add(3, 7)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Max of 3, 7, 2, 9: {get_max(3, 7, 2, 9)}")
    
    print("\nApply Operation ")
    numbers = [1, 2, 3, 4, 5]
    print(f"Squares: {apply_operation(numbers, lambda x: x ** 2)}")
    
    print("\nFilter Data ")
    print(f"Even numbers: {filter_data(numbers, lambda x: x % 2 == 0)}")
    
    print("\nStatistics ")
    print(calculate_statistics(10, 20, 30, 40, 50))
    