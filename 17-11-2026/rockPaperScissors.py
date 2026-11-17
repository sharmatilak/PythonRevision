# Rock Paper Scissors Game

import random 

guesses = 0
totalGuesses = 2
choices = ("Rock", "Paper", "Scissors")
answer = random.choice(choices)
is_running = True

# print(answer)

while is_running:

    if guesses == totalGuesses:
        print(f"You used all your {totalGuesses} guesses bruh!")
        break
    else:
        pass
    guess = input("Choose between 1-3\n1. Rock\n2. Paper\n3. Scissors ")
    guess = guess.capitalize()

    if guess in choices:
        guesses += 1
        if guess == answer:
            print(f"Correct!\nIt took you {guesses} try(s) to guess!\n\n")
            break
        else:
            print(f"Try again!\nYou have {totalGuesses - guesses} left!\n\n")

    else:
        print("Invalid Response!\n\n")
        break