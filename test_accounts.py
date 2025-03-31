# test_accounts.py

from bank_accounts import SavingsAccount

def test_balance():
    account = SavingsAccount("TestUser")
    account.deposit(500)
    account.withdraw(100)
    account.apply_interest()
    assert account.get_balance() > 0

