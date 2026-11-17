# Dice Roller Program

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

import random

dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),

    2: ("┌─────────┐", 
        "│ ●       │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),

    3: ("┌─────────┐", 
        "│ ●       │", 
        "│    ●    │", 
        "│       ● │", 
        "└─────────┘"),

    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),

    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),

    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")
}


dices = []
total = 0

num_of_dice = int(input("How many dice you want? "))

for dice in range(num_of_dice):
    dices.append(random.randint(1,6))

for dice in range(num_of_dice):
    for line in dice_art.get(dices[dice]):
        print(line)

for dice in dices:
    total += dice

print(f"Total of dices: {total}")

# print(*dice_art[1], sep="\n")

# for line in dice_art.get(1):
#     print(line)