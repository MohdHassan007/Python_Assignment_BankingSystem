from entity.customer import Customer
from entity.account import Account,SavingsAccount, CurrentAccount


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_number, account_type, initial_balance=0.0):
        account = Account(account_number, account_type, initial_balance)
        self.accounts.append(account)
        print(f"Account created successfully: {account.get_account_number()}")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def calculate_interest(self, account_number):
        account = self.find_account(account_number)
        if account and account.get_account_type().lower() == "savings":
            account.calculate_interest()
        else:
            print("Account not found or not a savings account.")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None



