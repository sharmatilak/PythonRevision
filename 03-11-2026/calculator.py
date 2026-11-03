operator = input("Enter an operator (+ - * /): ")

firstNumber = int(input("Enter the 1st number: "))
secondNumber = int(input("Enter the 2nd number: "))

if operator == "+":
    result = firstNumber + secondNumber
    print(f"Here is the result of addition: {result}.")
elif operator == "-":
    result = firstNumber - secondNumber
    print(f"Here is the result of subtraction: {result}.")
elif operator == "*":
    result = firstNumber * secondNumber
    print(f"Here is the result of multiplication: {result}.")
elif operator == "/":
    try:
        result = firstNumber / secondNumber
        print(f"Here is the result of division: {result}.")
    except ZeroDivisionError:
        print("You can not divide a number with 0.")
else:
    print("You chose wrong option gang.")
