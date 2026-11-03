# Python weight converter Program

weight = float(input("Enter the weight: "))

weightUnit = input("Is this weight in Kilograms or Pounds? (kg/lbs): ")

if weightUnit.lower() == "kg":
    if weight < 34 or weight == 0:
        print("You possibly can not have this weight bruh...")
    else:
        finalQues = input("Do you want to convert it into Pounds (Y/N): ")
        if finalQues.upper() == "Y":
            finalWeight = weight * 2.204623
            print(f"{weight} KG in pounds will be {finalWeight:.2f} lbs.")
        elif finalQues.upper() == "N":
            print("Thanks for stopping by.")
        else:
            print("Not the thing we asked for...")

elif weightUnit.lower() == "lbs":
    if weight < 75 or weight == 0:
            print("You possibly can not have this weight bruh...")
    else:
        finalQues = input("Do you want to convert it into Kilograms (Y/N): ")
        if finalQues.upper() == "Y":
            finalWeight = weight / 2.204623
            print(f"{weight} lbs in Kilograms will be {finalWeight:.2f} KG.")
        elif finalQues.upper() == "N":
            print("Thanks for stopping by.")
        else:
            print("Not the thing we asked for...")

else:
    print("Not the thing we asked for...")
