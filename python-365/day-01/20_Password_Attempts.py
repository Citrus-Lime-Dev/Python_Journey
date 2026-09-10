password = "python123"

for count in range(3):
    password_input = input("Password: ")

    if password_input == password:
        print("Login successful!")
        break
else:
    print("Account locked!")

