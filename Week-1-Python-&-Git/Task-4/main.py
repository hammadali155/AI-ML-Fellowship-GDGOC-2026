from modules import math_module, string_module
from mypackage import SimpleCalculator

def main():
    print("Math Module:")
    print(f"5 + 3 = {math_module.add(5, 3)}")
    print(f"10 / 2 = {math_module.divide(10, 2)}")
    print(f'\nStats: [1,5,10,20,30,4]')
    stats = math_module.calculate_stats([1,5,10,20,30,41])
    print(f'''Sum : {stats["sum"]}
Max: {stats["max"]}
Min : {stats["min"]}''')

    print("\nString Module:")
    print(f"Reverse 'hello': {string_module.reverse_text('hello')}")
    print(f"Uppercase 'world': {string_module.to_uppercase('world')}")

    print("\nMyPackage Calculator:")
    calc = SimpleCalculator()
    print(f"Calc Add 7 + 7: {calc.add_numbers(7, 7)}")
    print(f"Calc Multiply 3 * 4: {calc.multiply_numbers(3, 4)}")

if __name__ == "__main__":
    main()
