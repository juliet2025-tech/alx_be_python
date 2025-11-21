# pattern_drawing.py
# Draws a square pattern of asterisks of user-defined size

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
        return

    row = 0  # Start of while loop
    while row < size:
        # Nested for loop to print asterisks in a row
        for col in range(size):
            print("*", end="")  # Stay on the same line
        print()  # Move to next line after row is complete
        row += 1  # Increment the row

if __name__ == "__main__":
    main()
