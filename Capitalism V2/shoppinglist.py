from colorama import Fore, Back
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
try:
    with open("list", "r") as fp:
        list = json.load(fp)
    shoppingListData =  list
except Exception as error: print(f"{Fore.RED}Loading data FAILED. Did you run setup first?{Fore.RESET} Error Code:" + str(error))

def syncList():
    with open("list", "w") as fp:
        fp.write(json.dumps(shoppingListData))
    print("Succesfully wrote changes")

def fancyPrint():
    '''for item in shoppingListData:
        print(item.capitalize())'''
    print(Fore.MAGENTA + ", ".join(shoppingListData) + Fore.RESET )

def addItem():
    itemToAdd = input(Fore.BLUE + "What item?")
    shoppingListData.append(itemToAdd)
    print(Fore.GREEN + f"Succesfully added {itemToAdd} to the list {Fore.RESET}")
    syncList()
def removeItem():
    fancyPrint()
    itemToRemove = input(Fore.BLUE + "Remove which item?")
    shoppingListData.remove(itemToRemove)
    print(Fore.GREEN + f"Succesfully removed {itemToRemove} from the list {Fore.RESET}")
    syncList()

def clearList():
    shoppingListData = []
    syncList()

def mainMenu():
    print("""=========
Main Menu
=========""")
    print("1. Print List")
    print("2. Add Item")
    print("3. Remove Item")
    print(f"{Back.RED}{Fore.GREEN}4. Clear List{Fore.RESET}{Back.RESET}")
    mainmenuinput = input("")
    return mainmenuinput

while True:
    a = int(mainMenu())
    if a == 1:
        fancyPrint()
    if a == 2:
        addItem()
    if a == 3:
        removeItem()
print(Fore.RESET)
print(Back.RESET)