secret = 5
count = 0

while True:
    user_input = int(input("Guess the secret number (1-10) : "))
    if 1 <= user_input <= 10:
        count += 1
        if user_input == secret:
            break
        else:
            if user_input < secret:
                print("Too low")
            else:
                print("Too high")
    else:
        print("Please enter a number between 1 and 10")

print(f"Congrats!!! You guessed the number in {count} chances.")