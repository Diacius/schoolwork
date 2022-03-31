from colorama import Fore, Back
print("Capitalism V2 Patch Notes:")
print(" - Ended Communism")
print(" - Fixed bug that allowed poor people to buy food")

print(f"""{Fore.BLUE}{Back.RESET}
===========
|Shopping |
|List     |
===========
""")

print("Loading data....")
import json
try:
    with open("list", "r") as fp:
        list = json.load(fp)
    print(list)
except:
    print(f"{Fore.RED}Loading data FAILED. Did you run setup first?{Fore.RESET}")


print("Exiting")
print(Fore.RESET)
print(Back.RESET)