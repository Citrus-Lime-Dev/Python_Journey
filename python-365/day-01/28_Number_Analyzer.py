def check_sign(num):
        if num < 0:
            return "Negative"
        elif num == 0:
            return "Zero"
        else:
            return "Positive"

def is_even(num):
    if num % 2 == 0:
        return True
    return False

def calculate_square(num):
        return num ** 2

def calculate_cube(num):
    return num ** 3

user_num = int(input("Enter a number: "))
print(f"Sign: {check_sign(user_num)}")
print(f"Even/Odd: {'Even' if is_even(user_num) else 'Odd'}")
print(f"Square: {calculate_square(user_num)}")
print(f"Cube: {calculate_cube(user_num)}")