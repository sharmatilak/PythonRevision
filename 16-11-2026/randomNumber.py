import random

low = 1
high = 100

number = random.randint(low, high)

guesses = 0

while True:
    userNumber = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    if userNumber == number:
        print("Wow you guessed it right! ")
        print(f"It took you {guesses} tries to guess!\nWell done!\n\n")
        break
    elif userNumber > number:
        print(f"Your guessed number is higher than the actual number\nPlease choose smaller number.")
        print(f"Total guesses remaining: {6 - guesses}/6\n\n")
    elif userNumber < number:
        print(f"Your guessed number is lower than the actual number\nPlease choose bigger number.")
        print(f"Total guesses remaining: {6 - guesses}/6\n\n")

    elif guesses == 6:
        print("You used all your guesses,\nIt is okay try again later buddy!")

    else:
        print("Please type a valid response...\n\n")




