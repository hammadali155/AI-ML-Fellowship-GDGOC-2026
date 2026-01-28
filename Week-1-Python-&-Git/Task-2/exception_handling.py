def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None
    except TypeError:
        print("Error: Please provide numeric values!")
        return None
    else:
        print(f"Division successful: {a} / {b} = {result}")
        return result
    finally:
        print("Division operation completed.\n")


def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise
        finally:
            pass


def calculate(num1, num2, operation):
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError(f"Invalid operation: {operation}")
    
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        print(f"Result: {num1} {operation} {num2} = {result}")
        return result
    finally:
        print("Calculation completed.\n")


def advanced_calculator():
    print("="*50)
    print("EXCEPTION-SAFE CALCULATOR")
    print("="*50)
    
    history = []
    
    while True:
        try:
            print("\nOperations: +, -, *, /")
            print("Type 'history' to view calculation history")
            print("Type 'quit' to exit\n")
            
            operation = input("Enter operation (+, -, *, /) or command: ").strip()
            
            if operation.lower() == 'quit':
                print("Goodbye!")
                break
            
            if operation.lower() == 'history':
                if history:
                    print("\nCalculation History:")
                    for i, calc in enumerate(history, 1):
                        print(f"{i}. {calc}")
                else:
                    print("No history available.")
                continue
            
            if operation not in ['+', '-', '*', '/']:
                raise ValueError(f"Invalid operation: {operation}")
            
            num1 = get_numeric_input("Enter first number: ")
            num2 = get_numeric_input("Enter second number: ")
            
            result = calculate(num1, num2, operation)
            
            if result is not None:
                history.append(f"{num1} {operation} {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
        finally:
            pass




def main():
    advanced_calculator()

if __name__ == "__main__":
    main()
