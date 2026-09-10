def is_even(num):
    if num % 2 == 0:
        return True
    return False

user_num = int(input("Enter a number: "))
if is_even(user_num):
    print(f"{user_num} is even")
else:
    print(f"{user_num} is odd")