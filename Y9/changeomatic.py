from colorama import Fore, Back
print(f"{Fore.CYAN}==={Fore.GREEN}ChangeOMatic{Fore.CYAN}==={Fore.RESET}")
while True:
    while True:
        itemcosts = input(f"{Fore.YELLOW}How much is the bill enter as £s eg. 5.23 DO NOT INCLUDE THE SIGN{Fore.RESET}")
        if '£' in itemcosts:
            print(f"{Fore.RED}please do not include the £ sign{Fore.RESET}")
            break
        try:
            itemcosts = float(itemcosts)
            itemcosts = itemcosts / 100 # Make it in pennies            
        except:
            print(f"{Fore.RED}An error occurred trying to process the item cost check the format{Fore.RESET}")
            break

        customerpaid = input(f"{Fore.YELLOW}How much did the customer pay? enter as £s eg. 5.23 DO NOT INCLUDE THE SIGN{Fore.RESET}")
        try:
            customerpaid = float(customerpaid)
            customerpaid = customerpaid / 100 # Make it in pennies            
        except:
            print(f"{Fore.RED}An error occurred trying to process the customer payment check the format{Fore.RESET}")
            break
        if itemcosts == customerpaid :
            print(f"{Fore.GREEN}Customer paid correct amount{Fore.RESET}")
        if customerpaid < itemcosts:
            diff = itemcosts - customerpaid
            print(f"{Fore.RED}Customer needs to pay £{diff*100:.2f} more{Fore.RESET}")
        if customerpaid > itemcosts:
            print(f"{Fore.CYAN}Calculating Change....{Fore.RESET}")
            totalChange = customerpaid - itemcosts
            print(f"{Fore.GREEN}Total Change £{totalChange * 100:.2f}{Fore.RESET}")
            print("DBG" + totalChange)
            if totalChange % 100 == 0:
                a = totalChange % 100
                print(f"Give £{a}")
    print("Program looped due to  or failiure")