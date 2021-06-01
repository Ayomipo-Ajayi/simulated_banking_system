from abc import  ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def aunthenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayAmount():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccount = {}
    def create(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccount[self.accountNumber] = [name, initialDeposit]
        print(f"Account creatin has been successful. Your account number is {self.accountNumber}")
    def aunthenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication Successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccount[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingsAccount[self.accountNumber][1] -= withdrawalAmount
            print(f"Withdraw was successful")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccount[self.accountNumber][1] += depositAmount
    def displayAmount(self):
        print(f"Available balance: {self.savingsAccount[self.accountNumber][1]}")

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice == 1:
        print("Enter your name")
        name = input()
        print("Enter the initial deposit")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice == 2:
        print("Enter your name")
        name = input()
        print("Enter your account number")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.aunthenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                if userChoice == 1:
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice == 2:
                    print("Enter deposit amount")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice == 3:
                    savingsAccount.displayAmount()
                elif userChoice == 4:
                    break
    elif userChoice == 3:
                quit()


