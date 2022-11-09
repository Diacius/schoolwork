from colorama import init
from termcolor import colored
# use Colorama to make Termcolor work on Windows too
init()

print("---Welcome to SPLIT MY PIZZA™---")
people = int(input("num people"))
slices = int(input("how many slices do u want"))

# Calc slices
totalSlices = slices // people
if not people % slices == 0:
    slicesLeftOver = slices % people
else:
    slicesLeftOver = 0
print(colored(f'{people} people each get {totalSlices} slices with {slicesLeftOver} left over', "green"))
