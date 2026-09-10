def calculate_bill(price, num_of_items, tax_rate):
    sub_total = price * num_of_items
    tax = (sub_total * tax_rate)/ 100
    final_bill = sub_total+ tax

    return final_bill

item_price = float(input("What is the price of the item? "))
quantity = int(input("What is the quantity? "))
tax_percent = float(input("What is the tax percentage of your item? "))

total_bill = calculate_bill(item_price, quantity, tax_percent)
print(f"Total Bill = {total_bill:.2f}")