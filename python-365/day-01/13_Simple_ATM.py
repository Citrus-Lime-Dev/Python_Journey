balance = 10000

while True:
    user_input = int(input('''
    1 - Check Balance
    2 - Deposit Amount
    3 - Withdraw Amount
    4 - Exit
    Enter an option from the above: '''))

    if user_input <= 0 or user_input > 4:
        print("Invalid option")
    else:
        match user_input:
            case 1:
                print(f"Your balance is {balance}")

            case 2:
                deposit_amount = int(input("Enter amount to deposit: "))
                if deposit_amount >= 100:
                    balance += deposit_amount
                    print(f"Successfully deposited {deposit_amount}")
                else:
                    print("Please enter an amount above 100 to deposit")

            case 3:
                withdraw_amount = int(input("Enter amount to withdraw: "))
                if withdraw_amount <= 0:
                    print("Please enter an amount above 0 to withdraw")
                elif withdraw_amount > balance:
                    print("Insufficient funds")
                else:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew {withdraw_amount}")

            case 4:
                 break