'''
Simple accounts management system in Python without OOP
'''

accountNo = input("Enter Account # : ")
customerName = input("Enter Name : ")
accountType = input("Enter Account Type : ")
balance = float(input("Enter Balance # : "))

def withdraw(balance,amount):
    if accountType == "SAVINGS":
        newBalance = balance - amount
        if newBalance < 500 :
            print("Sorry, you do not have sufficient balance ")
        else:
            balance = newBalance
            print(f"You have successfully withdrawn {amount}. Your new balance is  {balance}")
            return balance
    elif accountType == "CURRENT":
        balance -= amount
        if balance < 0:
            print(f"Sorry you do not have sufficient funds to withdraw {amount}")
        else:
            print(f"You have successfully withdrawn {amount}. Your new balance is  {balance}")
        return balance

withdraw(balance,1000)