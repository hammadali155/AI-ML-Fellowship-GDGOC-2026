import time
import functools


def execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_duration = end_time - start_time
        
        print(f" Function '{func.__name__}' executed in {execution_duration:.6f} seconds")
        return result
    
    return wrapper


def timer_with_message(message="Execution completed"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            print(f" {message}: {end_time - start_time:.6f}s")
            return result
        return wrapper
    return decorator


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__}() returned {result!r}")
        
        return result
    return wrapper


def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {func.__name__}{args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i + 1}/{times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def validate_types(**type_hints):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import inspect
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            
            for param_name, expected_type in type_hints.items():
                if param_name in bound_args.arguments:
                    value = bound_args.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Parameter '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


def rate_limit(max_calls, time_window):
    calls = []
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            while calls and calls[0] < current_time - time_window:
                calls.pop(0)
            
            if len(calls) >= max_calls:
                print(f"Rate limit exceeded! Max {max_calls} calls per {time_window}s")
                return None
            
            calls.append(current_time)
            return func(*args, **kwargs)
        
        return wrapper
    return decorator


@execution_time
def slow_function():
    print("Starting slow function...")
    time.sleep(1)
    print("Slow function completed!")
    return "Done"


@timer_with_message("Matrix multiplication completed")
def matrix_multiply(size):
    matrix = [[1 for _ in range(size)] for _ in range(size)]
    result = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += matrix[i][k] * matrix[k][j]
    
    return result


@debug
def add_numbers(a, b):
    return a + b


@memoize
@execution_time
def fibonacci_memo(n):
    if n < 2:
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


@validate_types(name=str, age=int)
def create_profile(name, age):
    return {"name": name, "age": age}


@rate_limit(max_calls=3, time_window=5)
def api_call(endpoint):
    print(f"API call to {endpoint} successful")
    return {"status": "success", "endpoint": endpoint}


@execution_time
@debug
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


@execution_time
@memoize
def expensive_operation(n):
    time.sleep(0.5)
    return n ** 2


def demonstrate_decorators():
    print("="*60)
    print("DECORATOR DEMONSTRATIONS")
    print("="*60)
    
    print("\n1Execution Time Decorator:")
    slow_function()
    
    print("\nCustom Message Timer:")
    matrix_multiply(50)
    
    print("\nDebug Decorator:")
    add_numbers(5, 7)
    
    print("\nMemoization Decorator:")
    print("First call:")
    result1 = fibonacci_memo(10)
    print(f"Result: {result1}")
    print("\nSecond call (cached):")
    result2 = fibonacci_memo(10)
    print(f"Result: {result2}")
    
    print("\nRepeat Decorator:")
    greet("Hammad")
    
    print("\nType Validation Decorator:")
    try:
        profile = create_profile("Hammad Ali", 20)
        print(f"Profile created: {profile}")
        
        invalid_profile = create_profile("Hammad", "twenty")
    except TypeError as e:
        print(f"Type error caught: {e}")
    
    print("\nRate Limiting Decorator:")
    for i in range(5):
        api_call(f"/api/data/{i}")
        time.sleep(0.5)
    
    print("\nMultiple Decorators (Stacking):")
    result = factorial(5)
    print(f"Factorial result: {result}")
    
    print("\nExpensive Operation (Cached):")
    print("First call:")
    expensive_operation(10)
    print("Second call (cached):")
    expensive_operation(10)
    
    print("\n" + "="*60)
    print("All Decorator Demonstrations Complete!")
    print("="*60)


if __name__ == "__main__":
    demonstrate_decorators()
