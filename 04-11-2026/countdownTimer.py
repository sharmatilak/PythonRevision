import time

my_time = int(input("Enter the time in seconds: "))

# for i in reversed(range(1, (my_time+1))): both are correct lol
for i in range(my_time, 0, -1):
    seconds = i % 60 # 3650 % 60 = 50 seconds
    # or minutes = (i // 60) % 60 would work because // rounds the number down to the lower integer unlike / which provides a float
    minutes = int(i / 60) % 60 # (3650/60) % 60 = (60.83) % 60 = 0 minutes
    hours = int(i/3600) # 3650/3600 = 1 hour
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
    

print("TIME IS UP!")

