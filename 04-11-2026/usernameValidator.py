# Username validator program

message = "" \
"Enter your username:\n" \
"1. Username must be less than 12 characters.\n" \
"2. Username must not contain no spaces.\n" \
"3. Username must not contain numbers. \n\n"
username = input(message)

if len(username) >= 12 and (not username.find(" ")) and username.isalpha():
    print("Thanks for following rules lol.")
else:
    print("Get out of here.")