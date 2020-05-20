Make a Python ATM that will:

- Assign the user a random balance at the start of the program
- Give the user a menu of options that include Checking Balance, making a Deposit, making a Withdraw, and Exiting the ATM
- Deposit and Withdraw should update the balance accordingly!
- They should not be able to withdraw more money than they have in their balance.
- Keep asking the user what they want to do until they exit the ATM

Try to incorporate functions for major parts of the ATM - specifically, running the menu, checking the balance, 
making withdraws/deposits/etc.

IMPORTANT TIPS:
- Use while loops
- You must define functions using def NameofFunc + must be at the top (before any other code a=or variables)
- Use int in order to get intergers

Helper code:

import random
global variableName

def checkAge(age):
    while True:
        if age > 0 and age < 18:
            return "adult"
            break
        elif age >=18 and age < 120:
            return "child"
            break
        else:
            print("Idk if that's an age.")
            age = int(input("What is your age?"))

#code run beneath definitions

print(random.randint(0,100))

# age = int(input("What is your age?"))
# status = checkAge(age)
# print(status)

# while True:
#     if age > 0 and age < 18:
#         print("You're a child!")
#         break
#     elif age >=18 and age < 120:
#         print("You're an adult.")
#         break
#     else:
#         print("Idk if that's an age.")
#         age = int(input("What is your age?"))
