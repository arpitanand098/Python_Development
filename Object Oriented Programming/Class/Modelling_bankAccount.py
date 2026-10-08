class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} is deposited. Your new Balance is {self.balance}")    

    def withdraw(self, amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn. Your new Balance is {self.balance}")

    def get_balance(self):
        return self.balance

## Create an Object 
account = BankAccount("Arpit", 5000)
print(account.balance)

## Call the instance methods
account.deposit(3480)
account.withdraw(1000)
print(account.get_balance())