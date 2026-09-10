item_price = float(input("What is the price of the item? "))
quantity = int(input("What is the quantity? "))
tax_percent = float(input("What is the tax percentage of your item? "))

sub_total = item_price * quantity
tax = (sub_total * tax_percent)/ 100
final_bill = sub_total+ tax

print(f"Sub Total = {sub_total}")
print(f"Tax = {tax}")
print(f"Final Bill = {final_bill:.2f}")