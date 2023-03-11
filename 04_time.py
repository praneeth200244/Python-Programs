import time

print("Time:", time.strftime('%H:%M:%S'))
timestamp = int(time.strftime('%H'))
print(timestamp)

if (timestamp > 3 and timestamp < 11):
    print("Good morning....")
elif (timestamp < 15):
    print("Good afternoon")
elif (timestamp < 18):
    print("Good evening")
else:
    print("Good night")
