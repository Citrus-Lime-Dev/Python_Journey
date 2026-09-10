from datetime import date

birth_year = int(input("What is your birth year? "))
current_year = date.today().year
print(f"Current year is {current_year}")

if birth_year <= current_year:
    print(f"Your age is {current_year - birth_year} ")
else:
    print("Please enter an year which is less than or equal to current year!")