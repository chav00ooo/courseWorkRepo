def addition_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print(f"The result of adding {num1} and {num2} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    addition_calculator()