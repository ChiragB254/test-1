def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
            
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        
        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# Run the calculator
calculator()
