'''
Password guessing game by George Prime 
Started 6/12/2022
Finished 6/12/2022 16:22
'''
correctPassword = input("Anna, please enter the correct password")
guesserName = input("What is your name.")
attempts = 0
print("Welcome to the Password Guessing Game. You have 8 attempts to guess my password. Good Luck!")
for i in range(8):
    userguess = input(f"What is the password {guesserName}")
    if userguess == correctPassword:
        print("Well done!")
        print(f"It took you {attempts} attempts to guess the passsword!")
        break
    else:
        print("Try again!")
        attempts =+ 1