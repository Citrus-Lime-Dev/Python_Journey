count = int(input("Enter a number: "))

if count <= 0:
    print("Please enter a positive integer greater than zero")

else:
    for i in range(count, 0, -1):
        print(i)

    print("Blast off!")