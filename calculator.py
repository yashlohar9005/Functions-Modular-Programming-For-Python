#A simple calculator module with basic arithmetic operations.

def add(a, b=0):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b=0):
    """Return the difference of two numbers."""
    return a - b


def multiply(a, b=1):
    """Return the product of two numbers."""
    return a * b


def divide(a, b=1):
    """Return the quotient of two numbers. Handles division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def get_user_input():
    """Get two numbers from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b


def display_menu():
    """Display calculator menu."""
    print("\nCalculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


def calculate(choice, a, b):
    """Perform calculation based on user choice."""
    if choice == "1":
        return add(a, b)
    elif choice == "2":
        return subtract(a, b)
    elif choice == "3":
        return multiply(a, b)
    elif choice == "4":
        return divide(a, b)
    else:
        return "Invalid choice"


def main():
    """Main function to run the calculator."""
    display_menu()
    choice = input("Enter your choice (1-4): ")
    a, b = get_user_input()
    result = calculate(choice, a, b)
    print("Result:", result)



# Independent Testing
def test_functions():
    """Test each function independently."""
    print("Testing add:", add(10, 5))
    print("Testing subtract:", subtract(10, 5))
    print("Testing multiply:", multiply(10, 5))
    print("Testing divide:", divide(10, 5))
    print("Testing divide by zero:", divide(10, 0))


if __name__ == "__main__":
    main()
    #test_functions()
