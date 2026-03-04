from abc import ABC,abstractmethod
class BankAccount(ABC):
    def checkbalance(self):
        print("you can checkout your balance")

    @abstractmethod
    def deposit(self):
        pass
    def withdraw(self):
        pass

class SavingsAccount(BankAccount):
    def deposite(self):
        print("2 lakhs per day")
    def withdraw(self):
        print("1 lakh you can withdraw")

class JointAccount(BankAccount):
    def deposite(self):
        print("only those 2 people can deposite")
    def withdraw(self):
        print("1 to 2 lakhs per day")
class CurrentAccount(self):
    def deposite(self):
        print("unlimited deposite")
    def withdraw(self):
        print("unlimited withdraw")

class SalaryAccount(self):
    def deposite(self):
        print("no limit")
    def withdraw(self):
        print("20T - 1L per day")

class PentionAccount(self):
    def deposite(self):
        print("no deposite")
    def withdraw(self):
        print("40T per day")

print("-----------abhinandhan--------")
abhinandhan=SavingsAccount()
abhinandhan.checkbalance()
abhinandhan.deposite()
abhinandhan.withdraw()

print("--------praveen----------")
praveen=currentAccount()
praveen.checkbalance()
praveen.deposite()
praveen.withdraw()

print("---saaketh_nikhil---")
saaketh_nikhil=JointAccount()
saaketh_nikhil.checkbalance()
saaketh_nikhil.deposit()
saaketh_nikhil.withdraw()

print("---shanmukh---")
shanmukh=SalaryAccount()
shanmukh.checkbalance()
shanmukh.deposit()
shanmukh.withdraw()

print("---swapnil---")
swapnil=PensionAccount()
swapnil.checkbalance()
swapnil.deposit()
swapnil.withdraw()

