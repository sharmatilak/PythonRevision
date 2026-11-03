# Temperature Conversion Program

c_or_f = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

if c_or_f.lower() == "c":
    temperature = int(input("Enter the temperature: "))
    temp_in_f = (9/5) * temperature + 32
    final_temp = print(f"{temperature}°C in Fahrenheit will be {temp_in_f}°F.")
elif c_or_f.lower() == "f":
    temperature = int(input("Enter the temperature: "))
    temp_in_c = (5/9) * (temperature - 32)
    final_temp = print(f"{temperature}°F in Celsius will be {temp_in_c}°C.")
else:
    print("What??? I don't know what you are talking about man...")