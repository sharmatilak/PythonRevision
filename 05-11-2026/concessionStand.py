# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")


while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) == None:
        print("This item is not in the menu.")
    else:
        cart.append(food)
    for item in cart:
        price = menu.get(item)
        total += price

print("You purchased: \n")
i = 1
for item in cart:
    print(f"{i}. {item:10} - ${menu.get(item)}")
    i += 1

print(f"Your Total is ${total:.2f}")