class BankTransaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

def add_transaction():
    transaction_type = input("Enter transaction type (Deposit/Withdraw): ").capitalize()
    amount = float(input("Enter transaction amount: "))
    return BankTransaction(transaction_type, amount)

def main():
    transactions = []

    while True:
        choice = input("Do you want to add a transaction? (yes-1/no-2): ").lower()

        if choice == 'yes' or choice == '1':
            transaction = add_transaction()
            transactions.append(transaction)
        elif choice == 'no' or choice == '2':
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

    print("\nTransaction History:")
    for index, transaction in enumerate(transactions, start=1):
        print(f"{index}. {transaction.transaction_type}: ${transaction.amount}")

if __name__ == "__main__":
    main()
