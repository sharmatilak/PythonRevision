# Random Number Guessing Game

import random

lowest_num = 1
highest_num = 100

number = random.randint(lowest_num, highest_num)
random_threshold = random.randint(20,70)
guesses = 0

while True:
    userNumber = input("Guess a number between 1 and 100: ")

    if userNumber.isdigit():
        userNumber = int(userNumber)
        guesses += 1
        print(f"minus: {userNumber - number}\nactual number: {number}\n\n")

        if guesses > 6:
            print("Sorry buddy...You are out of guesses.\n\n")
            break
        else:
            pass

        if userNumber < lowest_num or userNumber > highest_num:
            print(f"Please select a number between {lowest_num} and {highest_num}.")
            print(f"You have {6 - guesses} guesses left!\n\n")

        elif userNumber == number:
            print(f"Yes {userNumber} is the correct guess!")
            print(f"It took you {guesses} tries to guess!")
            break

        elif (userNumber - number) > 0:
            if abs(userNumber - number) > random_threshold:
                print(f"{userNumber} is way greater than the actual number!")
                print(f"You have {6 - guesses} guesses left!\n\n")

            else:
                print(f"{userNumber} is greater than the actual number!")
                print(f"You have {6 - guesses} guesses left!\n\n")

            
        elif (userNumber - number) < 0:
            if abs(userNumber - number) > random_threshold:
                print(f"{userNumber} is way lesser than the actual number!")
                print(f"You have {6 - guesses} guesses left!\n\n")
            
            else:
                print(f"{userNumber} is lesser than the actual number!")
                print(f"You have {6 - guesses} guesses left!\n\n")
        else:
            print(f"Please select a number between {lowest_num} and {highest_num}\n\n")

    else:
        print(f"Please select a number between {lowest_num} and {highest_num}\n\n")




