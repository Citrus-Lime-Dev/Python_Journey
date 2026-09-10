def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return round(num1 / num2, 2)

result= ""

choice = int(input('''
    Welcome to the Calculator!
    1 - Add
    2 - Subtract
    3 - Multiply
    4 - Divide: '''))

if choice < 1 or choice > 4:
    print("Please enter a number between 1 and 4")
else:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    match choice:
        case 1:
            result = add(a, b)
            print(result)
        case 2:
            result = subtract(a, b)
            print(result)
        case 3:
            result = multiply(a, b)
            print(result)
        case 4:
            if b != 0:
                result = divide(a, b)
                print(result)
            else:
                print("Division by zero is not possible!")
        case _:
            print("Please enter a number between 1 and 4")