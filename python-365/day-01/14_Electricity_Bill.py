units_consumed = int(input("Enter the units consumed: "))
bill = 0

if units_consumed <= 0:
    print("How could you consume 0 units, are you God or an Indian Politician ?")

else:
    if units_consumed <= 100:
        bill = units_consumed * 2

    elif units_consumed <= 200:
        bill = 100 * 2 + (units_consumed - 100) * 3

    elif units_consumed <= 500:
            bill = (100 * 2) + (100 * 3) + (units_consumed - 200) * 5

    else:
            bill = (100 * 2) + (100 * 3) + (300 * 5) + (units_consumed - 500) * 7

    print(bill)