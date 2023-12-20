def calculate_future_balance(initial_balance, annual_interest_rate, years):
    # Calculate future balance using compound interest formula
    future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
    return future_balance

# Number of customers
num_customers = int(input("Enter the number of customers: "))

# Loop through each customer
for customer in range(1, num_customers + 1):
    print(f"\nCustomer {customer}:")

    # Get user input for initial balance, annual interest rate, and number of years
    initial_balance = float(input("Enter initial balance: $"))
    annual_interest_rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    # Calculate and display the future balance
    future_balance = calculate_future_balance(initial_balance, annual_interest_rate, years)
    print(f"Future balance after {years} years: ${future_balance:.2f}")
