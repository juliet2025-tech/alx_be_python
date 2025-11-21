# multiplication_table.py
# Prints the multiplication table for a given number

def main():
    # Step 1: Get user input
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input! Please enter an integer number.")
        return

    # Step 2: Generate and print multiplication table
    for i in range(1, 11):  # 1 to 10
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()
