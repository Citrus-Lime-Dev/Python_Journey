num = int(input("Enter a natural number to find out the multiplication table upto 10: "))

if num <= 0:
    print("Please enter a positive number greater than 0")

else:
    print(f"Multiplication Table for {num} upto 10 :")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")