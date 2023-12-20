class ATM:
    def __init__(self, current_balance):
        self.current_balance = current_balance

    def check_balance(self):
        print(f"Your current balance: ${self.current_balance}")

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.current_balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount % 100 == 0 and amount <= self.current_balance:
            self.current_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.current_balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")
        else:
            print("Insufficient funds for withdrawal.")


initial_balance = float(input("Enter your current balance: $"))
atm = ATM(initial_balance)

# Display ATM options
while True:
    print("\nATM Options:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        deposit_amount = float(input("Enter the deposit amount: $"))
        atm.deposit(deposit_amount)
    elif choice == 3:
        withdraw_amount = float(input("Enter the withdrawal amount: $"))
        atm.withdraw(withdraw_amount)
    elif choice == 4:
        print("Exiting ATM. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
