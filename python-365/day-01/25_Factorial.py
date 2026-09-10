num = int(input("Enter a number: "))
res = 1

if num > 0:
    for i in range (1, num + 1):
        res = res * i

    print(f"The factorial of {num} is {res}")

elif num == 0:
    print(f"The factorial of {num} is 1")

else:
    print(f"Please enter a positive integer")