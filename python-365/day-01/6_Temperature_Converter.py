temp_in_celsius = float(input("Enter your temperature in Celsius: "))
temp_in_fahrenheit = temp_in_celsius * 1.8 + 32
print(f"Your temperature in Fahrenheit is {temp_in_fahrenheit:.2f}")
reconverted_to_celsius = round((temp_in_fahrenheit - 32) / 1.8, 2)
print(f"Temperature is back to Celsius: {reconverted_to_celsius}")

if round(reconverted_to_celsius, 2) == round(temp_in_celsius, 2):
    print("The reconversion is successful")