# Python Banking Program


balance = 0.00

print("Welcome to the Python Banking Program.")

def show_balance():
    print(f"Your balance is: ${balance}\n\n")

def withdraw(amount):
    global balance
    if balance < amount:
        print("You do not have sufficient balance to withdraw!\n\n")
        
    else:
        balance = balance - amount
        print(f"You have withdrawn ${amount}\nYour current balance is ${balance}\n\n")

def deposit(amount):
    global balance
    balance += amount
    print(f"You have deposited ${amount}\nYour current balance is ${balance}\n\n")

def main(userInput):
    if userInput.isdigit():
        userInput = int(userInput)
        match userInput:
                case 1:
                    show_balance()
                case 2:
                    amount = input("Enter the amount you want to withdraw: ")
                    if not amount.isdigit():
                        print("Invalid input!")
                    else:
                        amount = float(amount)
                        withdraw(amount)
                case 3:
                    amount = input("Enter the amount you want to deposit: ")
                    if not amount.isdigit():
                        print("Invalid input!")
                    else:
                        amount = float(amount)
                        deposit(amount)
                case _:
                    print("Invalid input!")
    else:
        print("Invalid input")

    
while True:
    userInput = input("Select 1-3 (q for quit)\n1. Show Balance\n2. Withdraw money\n3. Deposit money ")
    if userInput.lower() == "q":
        print("Thank you for using my program.\n\n")
        break
    else:
        main(userInput)
# print(f"Remaining balance: ${balance}")