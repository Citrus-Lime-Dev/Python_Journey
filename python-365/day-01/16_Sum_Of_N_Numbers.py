num = int(input("Enter a natural number to find out the sum of numbers: "))
_sum = 0

if num <= 0:
    print("Sum of numbers = 0")

else:
    for i in range(1, num+1):
        _sum += i

    print(f"Sum of numbers till {num} = " + str(_sum))
