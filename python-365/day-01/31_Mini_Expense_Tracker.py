def expenses_list(expenses):
    list_of_expenses = []
    for i in range(expenses):
        expense = float(input(f"Enter expense {i + 1}: "))
        list_of_expenses.append(expense)
    return list_of_expenses

def total_expenses(expenses_list):
    sum_of_expenses = 0
    for expense in expenses_list:
        sum_of_expenses += expense

    return sum_of_expenses

def max_expense(expenses):
    max_exp = expenses[0]
    for expense in expenses:
        if expense > max_exp:
            max_exp = expense
    return max_exp

def summary(expense_list, whole_amount, highest_expense, avg_exp):
    print("\n========== EXPENSE SUMMARY ==========\n")
    print("Expenses:")
    for expense in expense_list:
        print(f"₹{expense:.2f}")
    print("\n")
    print(f"Total Expenses: ₹{whole_amount}")
    print(f"Highest Expense: ₹{highest_expense}")
    print(f"Average Expense: ₹{avg_exp}")

num_of_expenses = int(input("Enter number of expenses: "))

if num_of_expenses <= 0:
    print("Invalid number of expenses")
else:
    list_of_expenses = expenses_list(num_of_expenses)
    total_amount = total_expenses(list_of_expenses)
    maximum_expense = max_expense(list_of_expenses)
    average_expense = total_amount / num_of_expenses
    summary(list_of_expenses,total_amount, maximum_expense, average_expense)