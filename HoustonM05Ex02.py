#Generating random
import random

#Setting a variable to intiate the loop
tryAgain = "y"

while tryAgain == "y":

    number = random.randrange(100)+1 #Generating Numbers

    guess = int(input("Guess my number between 1 and 100: "))

    count = 1    #tracking the number of tries for user

    while guess != number:         #If number is too high

        if guess > number:

            print("Too high")

            guess = int(input("Guess again: "))

            count += 1

        elif guess < number:    #if number is to low

            print("Too low")

            guess = int(input("Guess again: "))

            count += 1

    print("You guessed the number!")

    print("You required "+str(count)+" tries.")    #Displaying tries

    tryAgain = input("Do you want to play again (y or n):")    #Asking user to continue the game

    if tryAgain != "y":
            print('Thanks for playing')
    else:
        tryAgain = 'y'






