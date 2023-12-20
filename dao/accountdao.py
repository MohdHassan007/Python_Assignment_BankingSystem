import mysql.connector
from util.DBconnUtil import DBConnUtil
from exception.exceptions import InsufficientBalanceError ,InvalidAccountException
class AccountDAO:
    def __init__(self):
        self.connection = DBConnUtil.open_connection()
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def deposit(self, account_number, amount):
        account_exists_query = "SELECT COUNT(*) FROM BANK.accounts WHERE account_number = %s"
        self.cursor.execute(account_exists_query, (account_number,))
        account_exists = self.cursor.fetchone()[0]

        if not account_exists:
            raise InvalidAccountException(f"Account with number {account_number} does not exist.")

        query = "UPDATE BANK.accounts SET account_balance = account_balance + %s WHERE account_number = %s"
        self.cursor.execute(query, (amount, account_number))
        self.connection.commit()



    def withdraw(self, account_number, amount):
        # Check the account type (savings or current) to apply specific rules
        account_type_query = "SELECT account_type FROM BANK.accounts WHERE account_number = %s"
        self.cursor.execute(account_type_query, (account_number,))
        account_type = self.cursor.fetchone()

        if account_type:
            account_type = account_type[0]

            # Retrieve account balance
            balance_query = "SELECT account_balance FROM BANK.accounts WHERE account_number = %s"
            self.cursor.execute(balance_query, (account_number,))
            result = self.cursor.fetchone()

            if result:
                account_balance = result[0]

                # Apply withdrawal rules based on account type
                if account_type == 'Savings':
                    # Check minimum balance for savings account
                    minimum_balance = 500  # Adjust the minimum balance as needed
                    if int(account_balance) - int(amount) >= minimum_balance:
                        self.update_balance(account_number, int(account_balance) - int(amount))
                        print("Withdrawal successful.")
                        return self.get_balance(account_number)
                    else:
                        print("Insufficient balance. Minimum balance violation.")
                        return None
                elif account_type == 'Current':
                    overdraft_limit = 5000  # Adjust the overdraft limit as needed
                    available_balance = account_balance + overdraft_limit

                    if amount <= available_balance:
                        self.update_balance(account_number, int(account_balance) - int(amount))
                        print("Withdrawal successful.")
                        return self.get_balance(account_number)
                    else:
                        print("Insufficient balance. Exceeds overdraft limit.")
                        return None
                else:
                    print("Unsupported account type.")
                    return None
            else:
                print("Account not found.")
                return None
        else:
            print("Account type not found.")
            return None

    def update_balance(self, account_number, new_balance):
        update_query = "UPDATE BANK.accounts SET account_balance = %s WHERE account_number = %s"
        self.cursor.execute(update_query, (new_balance, account_number))
        self.connection.commit()

    def get_balance(self, account_number):
        balance_query = "SELECT account_balance FROM BANK.accounts WHERE account_number = %s"
        self.cursor.execute(balance_query, (account_number,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def calculate_interest(self, account_number):
        query = "SELECT account_balance FROM BANK.accounts WHERE account_number = %s"
        self.cursor.execute(query, (account_number,))
        result = self.cursor.fetchone()

        if result:
            account_balance = result[0]
            interest_rate = 0.045
            interest_amount = float( account_balance) * float(interest_rate)
            self.deposit(account_number, interest_amount)
            print("Interest calculated and added.")
            result = self.get_account_details( account_number)
            print(f"New Balance{result['account_balance']}")
        else:
            print("Account not found.")


    def create_account(self, account_type, initial_balance, customer_id):
        query = "INSERT INTO BANK.accounts (account_type, account_balance, customer_id) VALUES (%s, %s, %s)"
        data = (account_type, initial_balance, customer_id)

        with self.connection.cursor() as cursor:
            cursor.execute(query, data)

        self.connection.commit()
        print("Account created successfully.")

    def get_account_details(self, account_number):
        query = """
            SELECT a.account_type, a.account_balance, c.customer_id, c.first_name, c.last_name
            FROM BANK.accounts a
            JOIN BANK.customers c ON a.customer_id = c.customer_id
            WHERE a.account_number = %s
        """
        self.cursor.execute(query, (account_number,))
        result = self.cursor.fetchone()

        if result:
            account_details = {
                'account_type': result[0],
                'account_balance': result[1],
                'customer_id': result[2],
                'customer_name': f"{result[3]} {result[4]}"
            }
            return account_details
        else:
            return None

    def transfer(self, sender_account_number, recipient_account_number, amount):
        # Check if sender has sufficient balance
        query = "SELECT account_balance FROM BANK.accounts WHERE account_number = %s"
        self.cursor.execute(query, (sender_account_number,))
        sender_balance = self.cursor.fetchone()
        try:
            if sender_balance and sender_balance[0] >= amount:
                # Withdraw from sender
                withdraw_query = "UPDATE BANK.accounts SET account_balance = account_balance - %s WHERE account_number = %s"
                self.cursor.execute(withdraw_query, (amount, sender_account_number))

                # Deposit to recipient
                deposit_query = "UPDATE BANK.accounts SET account_balance = account_balance + %s WHERE account_number = %s"
                self.cursor.execute(deposit_query, (amount, recipient_account_number))

                self.connection.commit()
                print("Transfer successful.")
            else:
                raise InsufficientBalanceError("Insufficient funds for the transfer.")
        except InsufficientBalanceError as e:
            print(f"Error: {e}")
