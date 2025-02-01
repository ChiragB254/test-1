def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
            
            operations = {'+': num1 + num2, '-': num1 - num2, '*': num1 * num2, '/': num1 / num2 if num2 != 0 else "Error: Division by zero is not allowed."}
            
            result = operations.get(operator, "Invalid operator. Please use +, -, *, or /.")
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

if __name__ == "__main__":
    calculator()
