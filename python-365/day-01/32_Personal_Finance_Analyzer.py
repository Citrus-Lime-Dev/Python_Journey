def calculate_total_income(monthly_salary, add_income):
    total_monthly_income = monthly_salary + add_income
    return total_monthly_income


def expense_categories():
    expenses = {
        "Housing": int(input("Housing/Rent: ")),
        "Food": int(input("Food: ")),
        "Transportation": int(input("Transportation: ")),
        "Utilities": int(input("Utilities: ")),
        "Healthcare": int(input("Healthcare: ")),
        "Entertainment": int(input("Entertainment: ")),
        "Shopping": int(input("Shopping: ")),
        "Other": int(input("Other: "))
    }

    return expenses


def calculate_total_expenses(expenses_list):
    total = 0

    for category, expense in expenses_list.items():
        total += expense

    return total


def calculate_savings(final_income, final_expenses):
    return final_income - final_expenses


def calculate_savings_rate(tot_savings, tot_income):
    if tot_income != 0:
        return (tot_savings / tot_income) * 100
    else:
        return 0


def find_highest_expense(expenses_dict):
    highest_category = None
    highest_amount = None

    for category, amount in expenses_dict.items():
        if highest_amount is None or amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category, highest_amount


def calculate_expense_percentages(expense, total_expense):
    if total_expense != 0:
        return (expense / total_expense) * 100
    else:
        return 0


def determine_financial_health(rate_of_savings):
    if rate_of_savings >= 30:
        return "EXCELLENT"
    elif rate_of_savings >= 20:
        return "GOOD"
    elif rate_of_savings >= 10:
        return "NEEDS IMPROVEMENT"
    else:
        return "CRITICAL"


def display_report(
        month_sal,
        add_inc,
        exp_list,
        tot_expenses,
        saving,
        save_rate,
        high_exp,
        total_income,
        financial_health
):
    print("""
========================================
       PERSONAL FINANCE ANALYZER
========================================
""")

    print("\nINCOME\n")
    print(f"Monthly Salary:    ₹{month_sal:.2f}")
    print(f"Additional Income: ₹{add_inc:.2f}")
    print(f"Total Income:      ₹{total_income:.2f}")

    print("\nEXPENSES\n")

    for category, amount in exp_list.items():
        percentage = calculate_expense_percentages(amount, tot_expenses)
        print(f"{category}: ₹{amount:.2f} ({percentage:.2f}%)")

    print("\n----------------------------------------")

    print(f"Total Expenses:  ₹{tot_expenses:.2f}")
    print(f"Savings:         ₹{saving:.2f}")
    print(f"Savings Rate:    {save_rate:.2f}%")

    category, value = high_exp

    print("\nHighest Expense:")
    print(f"{category} - ₹{value:.2f}")

    print("\nFinancial Health:")
    print(financial_health)

    if saving < 0:
        print("\n⚠️ WARNING: You are spending more than you earn.")
    elif save_rate < 10:
        print("\n⚠️ WARNING: Your savings rate is critically low.")
    elif save_rate >= 20:
        print("\n✓ Good job! Your savings rate is healthy.")


monthly_sal = float(input("Enter your monthly salary: "))
additional_income = float(input("Enter your additional income: "))

if monthly_sal <= 0:
    print("Enter a monthly salary greater than 0")

else:
    total_income = calculate_total_income(
        monthly_sal,
        additional_income
    )

    expense_list = expense_categories()

    total_expenses = calculate_total_expenses(
        expense_list
    )

    total_savings = calculate_savings(
        total_income,
        total_expenses
    )

    savings_rate = calculate_savings_rate(
        total_savings,
        total_income
    )

    highest_expense = find_highest_expense(
        expense_list
    )

    financial_health = determine_financial_health(
        savings_rate
    )

    display_report(
        monthly_sal,
        additional_income,
        expense_list,
        total_expenses,
        total_savings,
        savings_rate,
        highest_expense,
        total_income,
        financial_health
    )