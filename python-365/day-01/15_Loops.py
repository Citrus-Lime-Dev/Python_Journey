print("Numbers: ")

for num in range(1,101):
    print(num, end = ",")

print("\nEven Numbers : ")

for even_num in range(2,101,2):
    print(even_num, end = ",")

print("\nOdd Numbers : ")
for odd_num in range(1, 101, 2):
    print(odd_num, end = ",")

print("\n Multiples of 5: ")
for num in range(5, 101, 5):
    print(num, end = ",")