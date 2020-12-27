'''
Converting from Traditional python code to oop implementation:
 - Define the parameter used within the nested-if statement
 - The case exception or the value used for the condition should be converted as a derived class
 - The action statement or expressions of the if-statement or switch case will be the 
 definition for the method at the derived class
 - If the switch case consists of a default expression in other languages then that definition will become
 the virtual method at the base class.
 - If the default expression is not present in tn switch case, then the definition will become the 
 abstract method at the base class
 - If any common variables are used crossed all the switch expressions or conditions then that variables will become the
 variable or fields at the base class.
'''
from abc import ABC, abstractmethod

class Account(ABC):

    def __init__(self,accountNo,customName, accountType, balance):
        self.AccountNo = accountNo
        self.CustomerName = customName
        self.AccountType = accountType
        self.Balance = balance

    def __str__(self):
        return "Account No. : {}\n Customer Name : {}\n Account type : {}\n Balance : {}\n".format(self.AccountNo,self.CustomerName,self.AccountType, self.Balance)

    def deposit(self, amount):
        self.Balance += amount

    @abstractmethod
    def withdraw(self,amount): pass


class SavingsAccount(Account):
    def withdraw(self,amount):
        if (self.Balance - amount) < 500:
            print(f"Sorry, you do not have sufficient balance to withdraw {amount}. Account balance must be greater than 500 euros")
        else:
            self.Balance -= amount
            print(f"You have successfully withdrawn {amount}. Your new balance is  {self.Balance}")



class CurrentAccount(Account):
    
    def withdraw(self,amount):
        if (self.Balance - amount) < 0:
            print(f"Sorry you do not have sufficient funds to withdraw {amount}")
        else:
            self.Balance -= amount
            print(f"You have successfully withdrawn {amount}. Your new balance is  {self.Balance}")


savingsAc = SavingsAccount("101", "Jonah Munyira", "SAVINGS",1500)
print(savingsAc)
amount = float(input("Enter amount to be withdrawn : "))
savingsAc.withdraw(amount)

currentAc = CurrentAccount("103", "James Macharia", "CURRENT", 2000)
print(currentAc)
amount = float(input("Enter amount to be withdrawn : "))
currentAc.withdraw(amount)
