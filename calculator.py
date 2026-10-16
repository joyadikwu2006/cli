def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def main():
    while True:
        print("\n=== CLI CALCULATOR ===")
        print("+ Addition")
        print("- Subtraction")
        print("* Multiplication")
        print("/ Division")
        print("q Quit")

        choice = input("Choose an operation: ").strip()

        if choice == "q":
            print("Calculator closed.")
            break

        if choice not in ("+", "-", "*", "/"):
            print("Invalid choice. Try again.")
            continue

        try:
            a = float(input("Enter first number: ").strip())
            b = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid number entered. Please enter numeric values.")
            continue

        if choice == "+":
            result = add(a, b)
        elif choice == "-":
            result = subtract(a, b)
        elif choice == "*":
            result = multiply(a, b)
        elif choice == "/":
            if b == 0:
                print("Cannot divide by zero. Try again.")
                continue
            result = divide(a, b)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()
