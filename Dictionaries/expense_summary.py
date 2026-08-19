expenses = {}

n = int(input("Enter number of expenses: "))

for i in range(n):
    name = input(f"Enter expense {i + 1} name: ")
    amount = float(input(f"Enter amount for {name}: "))
    expenses[name] = amount

total = sum(expenses.values())
highest = max(expenses.values())
lowest = min(expenses.values())
average = total / len(expenses)

highest_expense = max(expenses, key=expenses.get)
lowest_expense = min(expenses, key=expenses.get)

print("\n--- Expense Summary ---")
print("Total Expenses:", total)
print("Average Expense:", average)
print("Highest Expense:", highest_expense, "-", highest)
print("Lowest Expense:", lowest_expense, "-", lowest)