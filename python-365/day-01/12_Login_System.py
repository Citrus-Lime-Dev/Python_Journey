username = "admin"
password = "python123"

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

if user_name == username and pass_word == password:
    print("Login Successful")

elif user_name == "" and pass_word == "":
        print("Username and Password cannot be empty")
elif user_name == username and (pass_word == "" or pass_word != password):
            print("Incorrect password")
else:
    print("Incorrect username")
