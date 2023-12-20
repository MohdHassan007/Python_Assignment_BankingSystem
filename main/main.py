from entity.customer import Customer
from entity.account import Account, SavingsAccount, CurrentAccount
from entity.Bank import Bank
from dao.accountdao import AccountDAO  # Import the AccountDAO class
from exception.exceptions import InsufficientBalanceError , InvalidAccountException
class BankApp:
    def __init__(self):
        self.bank = Bank()
        self.account_dao = AccountDAO()  # Create an instance of AccountDAO

    def main(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Details")
            print("6. Exit")
            print("7.calculate interest")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.transfer()
            elif choice == "5":
                self.get_account_details()
            elif choice == "6":
                print("Exiting the Banking System. Goodbye!")
                self.account_dao.close_connection()  # Close the database connection
                break
            elif choice == "7":
                self.calculate_interest()
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

    def create_account(self):
        print("\nCreating a new account:")
        account_number = int(input("Enter account number"))
        customer = self.get_customer_info()
        account_type = self.get_account_type()

        if account_type.lower() == "savings":
            interest_rate = float(input("Enter the interest rate for the savings account: "))
            account = SavingsAccount(account_number, account_type, 500, interest_rate)
        elif account_type.lower() == "current":
            overdraft_limit = 1000
            account = CurrentAccount(account_number, account_type, 0.0, overdraft_limit)
        else:
            print("Invalid account type.")
            return

        account.customer = customer  # Set the customer for the account
        self.bank.create_account(account.get_account_number(), account_type, 0.0)
        self.account_dao.create_account( account_type,0,  customer.get_customer_id())
        print("Account created successfully.")

    def deposit(self):
        try:
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            self.account_dao.deposit(account_number, amount)
            print("Deposit successful.")
        except InvalidAccountException as e:
            print(f"Account {account_number}not found")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter withdrawal amount: "))
        self.account_dao.withdraw(account_number, amount)

    def transfer(self):
        try:
            sender_account_number = int(input("Enter your account number: "))
            recipient_account_number = int(input("Enter recipient's account number: "))
            amount = float(input("Enter transfer amount: "))
            self.account_dao.transfer(sender_account_number, recipient_account_number, amount)
            print("Transfer successful.")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")


    def get_account_details(self):
        account_number = int(input("Enter account number: "))
        details = self.account_dao.get_account_details(account_number)
        if details:
            print("\nAccount Details:")
            print(f"Account Type: {details['account_type']}")
            print(f"Customer ID: {details['customer_id']}")
            print(f"Customer Name: {details['customer_name']}")
            print(f"Balance: ${details['account_balance']}")
        else:
            print("Account not found.")

    def get_customer_info(self):
        customer_id = int(input("Enter customer ID: "))
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        address = input("Enter address: ")

        customer = Customer(customer_id, first_name, last_name, email, phone_number, address)
        return customer

    def get_account_type(self):
        while True:
            print("\nSelect Account Type:")
            print("1. Savings")
            print("2. Current")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "1":
                return "Savings"
            elif choice == "2":
                return "Current"
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def calculate_interest(self):
        account_number = int(input("Enter account number: "))
        self.account_dao.calculate_interest(account_number)


if __name__ == "__main__":
    bank_app = BankApp()
    bank_app.main()
