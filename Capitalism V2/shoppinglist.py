from re import M
from colorama import Fore, Back
from pip import main
print("Capitalism V2 Patch Notes:")
print(" - Ended Communism")
print(" - Fixed bug that allowed poor people to buy food")

print(f"""{Fore.BLUE}
-----------
|Shopping |
|List     |
-----------
{Fore.RESET}""")
import json
def loadList():
    try:
        with open("list", "r") as fp:
            list = json.load(fp)
        return list
    except:
        print(f"{Fore.RED}Loading data FAILED. Did you run setup first?{Fore.RESET}")

def fancyPrint():
    shoppingListData = loadList()
    '''for item in shoppingListData:
        print(item.capitalize())'''
    print(Fore.MAGENTA + ", ".join(shoppingListData) + Fore.RESET )

def mainMenu():
    print("""=========
Main Menu
=========""")
    print("1. Print List")
    print("2. Add Item")
    print("3. Remove Item")
    mainmenuinput = input("")
    return mainmenuinput

while True:
    a = int(mainMenu())
    if a == 1:
        fancyPrint()
print(Fore.RESET)
print(Back.RESET)