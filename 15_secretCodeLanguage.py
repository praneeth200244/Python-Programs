import random
import string

# Taking input from the user
originalMessage = input("Enter your message: ")

n = int(input("Enter 1 for coding or 0 for decoding: "))
coding = True if (n == 1) else False

# Pre-processing
message = originalMessage.split(" ")

# Coding
if (coding):
    newMessage = []
    for word in message:
        if (len(word) < 3):
            reversedS = word[::-1]
            newMessage.append(reversedS)
        else:
            word = word[1:] + word[0]
            random_1 = ''.join(random.choices(string.ascii_letters, k=3))
            random_2 = ''.join(random.choices(string.ascii_letters, k=3))
            word = random_1 + word + random_2
            newMessage.append(word)
    print(" ".join(newMessage))
# Decoding
else:
    newMessage = []
    for word in message:
        if (len(word) < 3):
            reversedS = word[::-1]
            newMessage.append(reversedS)
        else:
            word = word[3:-3]
            word = word[-1] + word[:-1]
            newMessage.append(word)
    print(" ".join(newMessage))
