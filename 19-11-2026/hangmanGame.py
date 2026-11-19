# Python Hangman Game

import random

words = ["apple", "banana", "orange", "guava", "pomegranate"]

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

def display_art(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    hint = " ".join(hint)
    print(hint)

def display_answer(answer):
    answer = " ".join(answer)
    print(answer)

def main():
    answer = random.choice(words)
    wrong_guesses = 0
    hint = ["_"] * len(answer)
    
    is_running = True
    while is_running: 
        userAnswer = "".join(hint)
        if userAnswer == answer:
            print("Hurrah you won the game!")
            is_running = False
            break
        
        if wrong_guesses >= len(hangman_art) - 1:
            display_art(wrong_guesses)
            display_answer(answer)
            print("Sorry you are out of guesses!")
            is_running = False
            break

        display_art(wrong_guesses)
        display_hint(hint)
        guess = input("Enter the letter: ").lower()
        if len(guess) > 1 or guess.isdigit():
            print("Wrong input!")
            continue

        if guess in hint:
            print("You have already guessed this letter!")
            continue

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    continue
        
        else:
            wrong_guesses += 1
        

        
        
        



if __name__ == "__main__":
    main()