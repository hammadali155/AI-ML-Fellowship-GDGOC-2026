def fibonacci_generator(limit=None):
    a, b = 0, 1
    count = 0
    
    while limit is None or count < limit:
        yield a
        a, b = b, a + b
        count += 1


def custom_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    
    current = start
    
    if step > 0:
        while current < stop:
            yield current
            current += step
    elif step < 0:
        while current > stop:
            yield current
            current += step
    else:
        raise ValueError("Step cannot be zero")


def prime_generator(limit=None):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    count = 0
    num = 2
    
    while limit is None or count < limit:
        if is_prime(num):
            yield num
            count += 1
        num += 1


def factorial_generator(n):
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            factorial = 1
        else:
            factorial *= i
        yield (i, factorial)


def file_line_generator(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found")


def chunk_generator(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def infinite_counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step


def alternating_generator(*iterables):
    iterators = [iter(it) for it in iterables]
    while iterators:
        for it in iterators[:]:
            try:
                yield next(it)
            except StopIteration:
                iterators.remove(it)


def power_generator(base, max_power):
    for power in range(max_power + 1):
        yield base ** power


def filter_generator(iterable, condition):
    for item in iterable:
        if condition(item):
            yield item


def map_generator(iterable, transform):
    for item in iterable:
        yield transform(item)


def demonstrate_generator_expressions():
    print("\nGenerator Expressions:")
    
    squares = (x**2 for x in range(10))
    print(f"Squares: {list(squares)}")
    
    evens = (x for x in range(20) if x % 2 == 0)
    print(f"Evens: {list(evens)}")
    
    words = ["hello", "world", "python", "generator"]
    lengths = (len(word) for word in words)
    print(f"Word lengths: {list(lengths)}")


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


def demonstrate_generators():
    print("="*60)
    print("GENERATOR DEMONSTRATIONS")
    print("="*60)
    
    print("\nFibonacci Generator:")
    fib = fibonacci_generator(10)
    print(f"First 10 Fibonacci numbers: {list(fib)}")
    
    print("\nCustom Range Generator:")
    print(f"Range(0, 10, 2): {list(custom_range(0, 10, 2))}")
    print(f"Range(10): {list(custom_range(10))}")
    print(f"Range(10, 0, -1): {list(custom_range(10, 0, -1))}")
    
    print("\nPrime Number Generator:")
    primes = prime_generator(10)
    print(f"First 10 primes: {list(primes)}")
    
    print("\nFactorial Generator:")
    factorials = factorial_generator(6)
    for num, fact in factorials:
        print(f"{num}! = {fact}")
    
    print("\nChunk Generator:")
    data = list(range(1, 21))
    print(f"Data: {data}")
    chunks = chunk_generator(data, 5)
    for i, chunk in enumerate(chunks, 1):
        print(f"Chunk {i}: {chunk}")
    
    print("\nInfinite Counter:")
    counter = infinite_counter(start=100, step=5)
    print("First 5 values from infinite counter:")
    for _ in range(5):
        print(f"  {next(counter)}")
    
    print("\nAlternating Generator:")
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = ['x', 'y', 'z']
    alternating = alternating_generator(list1, list2, list3)
    print(f"Alternating: {list(alternating)}")
    
    print("\nPower Generator:")
    powers_of_2 = power_generator(2, 10)
    print(f"Powers of 2: {list(powers_of_2)}")
    
    print("\nFilter Generator:")
    numbers = range(1, 21)
    evens = filter_generator(numbers, lambda x: x % 2 == 0)
    print(f"Even numbers: {list(evens)}")
    
    print("\nMap Generator:")
    numbers = [1, 2, 3, 4, 5]
    squared = map_generator(numbers, lambda x: x ** 2)
    print(f"Original: {numbers}")
    print(f"Squared: {list(squared)}")
    
    demonstrate_generator_expressions()
    
    print("\nCustom Iterator Class:")
    iterator = CustomIterator(5)
    print(f"Squares using custom iterator: {list(iterator)}")
    
    print("\nMemory Efficiency:")
    import sys
    
    list_comp = [x**2 for x in range(10000)]
    print(f"List size: {sys.getsizeof(list_comp)} bytes")
    
    gen_exp = (x**2 for x in range(10000))
    print(f"Generator size: {sys.getsizeof(gen_exp)} bytes")
    print(f"Memory saved: {sys.getsizeof(list_comp) - sys.getsizeof(gen_exp)} bytes")
    
    print("\nChaining Generators:")
    fibonacci = fibonacci_generator(20)
    primes = prime_generator(10)
    
    even_fibs = filter(lambda x: x % 2 == 0, fibonacci)
    print(f"Even Fibonacci numbers: {list(even_fibs)}")
    
    print("\n" + "="*60)
    print("All Generator Demonstrations Complete!")
    print("="*60)


if __name__ == "__main__":
    demonstrate_generators()
