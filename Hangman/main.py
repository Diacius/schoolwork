from time import sleep
import random
from unicodedata import category

fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya'] 
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']


userGuessList = []
userGuesses = []
playGame = True
category = ""
continueGame = True

name = input("Enter your name")
print(f"Hello {name} its time to play.... HANGMAN")


while True:
    