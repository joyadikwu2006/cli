import json
import os

if os.path.exists("expenses.json"):
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
else:
    expenses = []
    
def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)    

while True:
    print("\n=== EXPENSE TRACKER ===")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Count expenses")
    print("q. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "q":
        save_expenses()
        print("Expense tracker closed.")
        break

    elif choice == "1":
        description = input("Enter expense description: ").strip()

        if not description:
            print("Description cannot be empty.")
            continue

        try:
            amount = float(input("Enter amount in naira: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        expense = {
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for index, expense in enumerate(expenses, start=1):
                print(
                    f"{index}. {expense['description']}: "
                    f"₦{expense['amount']:.2f}"
                )
    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total expenses: ₦{total:.2f}")            
    
    elif choice == "4":
        print(f"Number of expenses: {len(expenses)}")

    else:
        print("Invalid choice.")