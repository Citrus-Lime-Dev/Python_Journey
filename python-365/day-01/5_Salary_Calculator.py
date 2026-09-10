salary = float(input("Enter your annual salary in lakhs: "))

after_deduction = salary * 0.9
monthly_salary = after_deduction / 12

print(f"Annual Salary: {salary} LPA")
print(f"Annual Salary after 10% deduction: {after_deduction} LPA")
print(f"Monthly Salary after 10% deduction: {monthly_salary} LPA")