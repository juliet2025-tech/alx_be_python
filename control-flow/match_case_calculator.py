# match_case_calculator.py
# Simple calculator using Match Case

def main():
    # Step 1: Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    # Step 2: Get user input for operation
    operation = input("Choose the operation (+, -, *, /): ").strip()

    # Step 3: Match Case to handle operations
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result}.")
        case _:
            print("Invalid operation selected!")

if __name__ == "__main__":
    main()
