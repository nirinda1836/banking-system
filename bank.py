class BankAccount:
    def __init__(self,name,account_number, balance = 0):
        self.name = name
        self.account_number = account_number 
        self.balance = balance 
    def deposit(self,amount):
        self.balance += amount 
        print("balance: ", self.balance)
        print("deposited amount: ", amount)
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount 
            print("withdraw amount: ", amount)
            print("balance: ", self.balance)
    def display(self):
        print("account holder name:", self.name)
        print("account number: ", self.account_number)
        print("current balance: ", self.balance)
    def check_balance(self):
        print("current balance: ", self.balance)
