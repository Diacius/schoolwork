'''
The magic number guessing game.
Started at: 05th January 2022 17:11
George Prime
'''
import random

computersNumber = random.randint(1,100)
guesses = 0

while True:
    print("Welcome to the Magic Number guessing game! See how many guesses you take until you guess the magic number")
    guess = int(input("What is your guess?"))
    if guess == computersNumber:
        print("Well done!")
        break
    else:
        print(computersNumber)
        if guess > computersNumber:
            print("Too high! Try again")
            guesses += 1
            print(guesses)
        if guess < computersNumber:
            print("Too low! Try again")
            guesses += 1
            print(guesses)
print(f"It took you {guesses} attempts to guess the magic number!")