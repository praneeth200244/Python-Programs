import random

userPoints = 0
computerPoints = 0

# Deciding winner


def snakeWaterGun(userInput, computerInput):
    global userPoints
    global computerPoints
    if (userInput == computerInput):
        return
    elif (userInput == 2 and computerInput == 1):
        computerPoints += 1
    elif (userInput == 3 and computerInput == 2):
        computerPoints += 1
    elif (userInput == 1 and computerInput == 3):
        computerPoints += 1
    else:
        userPoints += 1

# Taking input from the user


def inputForGame():
    print("Enter\n1---->Snake\n2---->Water\n3---->Gun")
    userInput = int(input("Enter your choice: "))
    computerInput = random.randint(1, 3)
    print("User:", userInput, "\nComputer:", computerInput)
    snakeWaterGun(userInput, computerInput)


play = True
while play:
    inputForGame()
    print("Enter 0 if you want to quit. Otherwise enter 4")
    n = int(input("Enter your choice: "))
    if (n == 4):
        play = True
    else:
        print("Computer points: ", computerPoints)
        print("User points:", userPoints)
        if (userPoints > computerPoints):
            print("You win.....")
        elif (userPoints < computerPoints):
            print("You loose.....")
        else:
            print("The game is draw")
        play = False
