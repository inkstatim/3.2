# oop task

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    interest_rate = 0.05

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self._BankAccount__balance -= amount


account = SavingsAccount("Alice")
account.deposit(500)
account.withdraw(100)
account.apply_interest()

print(f"Final balance for {account.owner}: {account.get_balance():.2f}")
