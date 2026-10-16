
expenses = []


def add_expense():
    description = input("Enter expense description: ").strip()

    if not description:
        print("Error: Description cannot be empty.")
        return

    amount_text = input("Enter amount in naira: ").strip()

    try:
        amount = float(amount_text)
    except ValueError:
        print("Error: Enter a valid number.")
        return

    if amount <= 0:
        print("Error: Amount must be greater than zero.")
        return

    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n=== YOUR EXPENSES ===")
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']}: "
            f"₦{expense['amount']:.2f}"
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: ₦{total:.2f}")


def main():
    while True:
        print("\n=== EXPENSE TRACKER ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Expense tracker closed.")
            break
        else:
            print("Invalid choice. Choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
