class Bank:
    def __init__(self):
        self.accounts = {
            1001: 5000.0,
            1002: 7500.0,
            1003: 10000.0,
        }

    def check_balance(self, account_number):
        return self.accounts.get(account_number)

bank = Bank()

while True:
    try:
        account_number = int(input("Enter your account number: "))

        if account_number in bank.accounts:
            balance = bank.check_balance(account_number)
            print(f"Account Balance for Account {account_number}: ${balance:.2f}")
            break
        else:
            print("Invalid account number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")
