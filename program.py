# Ask the user to choose an operation.
operation = input("Choose '+': add or '-': subtract: ").strip()

# Read the first number from the user and convert it to a float.
num1 = float(input("Enter first number: "))

# Read the second number from the user and convert it to a float.
num2 = float(input("Enter second number: "))

# Check the user's choice.
if operation == "+":
    # If the choice is '+', add the two numbers.
    result = num1 + num2
elif operation == "-":
    # If the choice is '-', subtract the second number from the first.
    result = num1 - num2
else:
    # If the choice is anything else, show an error message.
    print("Invalid choice.")
    result = None

# Print the result only if the operation was valid.
if result is not None:
    print("Result:", result)
