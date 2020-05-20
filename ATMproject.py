import random

def checkBalance():
    print(f'Your balance is {balance}')

def Withdraw(balance):
    Wamount = int(input("How much money would you like to withdraw from your account?\n"))
    if Wamount <= balance:
        balance -= Wamount
        print(f"Your new balance is: {balance}")
        return balance
    else:
        print("Your balance is too low to make this withdraw. Try again")


def Deposit(balance):
    Damount = int(input("How much money would you like to deposit into your account? \n"))
    balance += Damount 
    print(f"Your new balance is: {balance}")
    return balance


def menu(balance):
    while True:
        print("Welcome! Choose the number of one of the options presented: \n1) Check my balance \n2) Make a withdraw \n3) Make a deposit \n4) EXIT ATM")
        Start = input("What would you like to do?\n")
        if Start == "1":
            balance = checkBalance()
            print(balance)
            return balance

        elif Start == "2":
            balance = Withdraw(balance)
            print(balance)
            return balance

        elif Start == "3":
            balance = Deposit(balance)
            print(balance)
            return balance

        elif Start == "4":
            print("Thank you for using our services today! :)")
            break
        else:
            print("That's not an option. Try again!")


balance = random.randint(0, 100000)
menu(balance)

# while Start != "4":
#     menu()
# checkBalance()
# balance = Withdraw(balance)
# checkBalance()













