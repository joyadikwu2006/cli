import json

expenses = [
    {"description": "Transport", "amount": 500},
    {"description": "Lunch", "amount": 1250}
]

with open("expenses.json", "w") as file:
    json.dump(expenses, file)

print("Expenses saved.")

with open("expenses.json", "r") as file:
    saved_expenses = json.load(file)

print(saved_expenses)