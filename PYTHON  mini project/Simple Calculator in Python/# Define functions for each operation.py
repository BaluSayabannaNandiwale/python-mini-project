# Define functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed"

# Main program to display menu and take user input
def main():
    while True:
        # Display the menu
        print("\nMenu:")
        print("1. TO PERFORM ADDITION")
        print("2. TO PERFORM SUBTRACTION")
        print("3. TO PERFORM MULTIPLICATION")
        print("4. TO PERFORM DIVISION")
        print("5. EXIT")

        # Take user input for choice
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Exiting the program. Goodbye!")
            break

        # Take user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the selected operation
        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
