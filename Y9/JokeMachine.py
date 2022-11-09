# jokeapi https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit
import requests
import json
from time import sleep
points = 0
for i in range(5):
    joke =requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=twopart")
    jokeJSON = str(joke.text)
    joke = json.loads(jokeJSON)
    #DEBUG: print(jokeJSON)
    print("Welcome to the jokebox see if you can guess the puchline!")
    print(joke["setup"])
    guess = input("Guess the punchline:")
    if guess == joke["delivery"]:
        print("Well done you guessed it :) \n The full joke is:")
        print("Q: " + joke["setup"])
        sleep(1)
        print("A: " + joke["delivery"])
        sleep(1)
        print("You get a point!")
        points = points + 1
    else:
        print("You didn't guess correctly :( \n The full joke is:")
        print("Q: " + joke["setup"])
        sleep(1)
        print("A: " + joke["delivery"])
print("You got:")
sleep(1)
print(str(points) + " Points!")

    
    
