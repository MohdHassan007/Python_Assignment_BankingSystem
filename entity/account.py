class Account:
    def __init__(self, account_number, account_type, account_balance):
        self.account_number = None
        self.account_type = account_type
        self.account_balance = account_balance

    def get_account_number(self):
        return self.account_number

    def get_account_type(self):
        return self.account_type

    def get_account_balance(self):
        return self.account_balance

    def set_account_number(self, account_number):
        self.account_number = account_number

    def set_account_type(self, account_type):
        self.account_type = account_type

    def set_account_balance(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited ${amount}. New balance: ${self.account_balance}")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.account_balance}")
        else:
            print("Insufficient funds. Withdrawal canceled.")

    def calculate_interest(self):
        interest_rate = 4.5  # Fixed interest rate
        interest_amount = (interest_rate / 100) * self.account_balance
        print(f"Interest calculated: ${interest_amount}")


class SavingsAccount(Account):
    def __init__(self, account_number, account_type, account_balance, interest_rate):
        super().__init__(account_number, account_type, account_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_amount = self.account_balance * (self.interest_rate / 100)
        self.account_balance += interest_amount
        print(f"Interest calculated and added. New balance: ${self.account_balance}")


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000  # Example overdraft limit, you can adjust it as needed

    def __init__(self, account_number, account_type, account_balance, overdraft_limit):
        super().__init__(account_number, account_type, account_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        available_balance = self.account_balance + self.overdraft_limit
        if 0 < amount <= available_balance:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.account_balance}")
        else:
            print("Invalid withdrawal amount or exceeding overdraft limit.")



