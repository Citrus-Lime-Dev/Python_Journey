def calculate_bonus(salary, rating):
    if salary > 0:
        if rating == 1:
            return 0
        elif rating == 2:
            return salary * 0.05
        elif rating == 3:
            return salary * 0.1
        elif rating == 4:
            return salary * 0.15
        elif rating == 5:
            return salary * 0.2
        else:
            print("Invalid rating")
            return None
    else:
        print("Invalid salary")
        return None


def calculate_gross_salary(salary, bonus):
    return salary + bonus

def calculate_monthly_salary(salary):
    return salary / 12 * 100000

emp_name = input("Enter your name: ")
basic_salary = float(input("Enter your basic salary: "))
perf_rating = int(input("Enter your performance rating (1-5): "))

if basic_salary <= 0:
    print("Invalid salary")

elif perf_rating < 1 or perf_rating > 5:
    print("Invalid performance rating")

else:
    bonus_amount = calculate_bonus(basic_salary, perf_rating)
    gross_salary = calculate_gross_salary(basic_salary, bonus_amount)
    monthly_gross = calculate_monthly_salary(gross_salary)

    print(f"Employee: {emp_name}")
    print(f"Basic salary: ₹{basic_salary:.2f} LPA")
    print(f"Bonus: ₹{bonus_amount:.2f} LPA")
    print(f"Gross Salary: ₹{gross_salary:.2f} LPA")
    print(f"Monthly Gross: ₹{monthly_gross:.2f}")
