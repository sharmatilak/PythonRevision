# Shopping Cart Program


foods = []
prices = []
total = 0
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for a {food}: $"))
        foods.append(food)
        prices.append(price)

for i in range(len(foods)):
    print(f"{foods[i]} is ${prices[i]}")

for price in prices:
    total += price

print(f"Your total is ${total}")