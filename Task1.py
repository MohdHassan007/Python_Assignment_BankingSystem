class Customer:
    def __init__(self, credit_score, annual_income):
        self.credit_score = credit_score
        self.annual_income = annual_income

def check_loan_eligibility(customer):
    # Eligibility criteria
    credit_score_threshold = 700
    annual_income_threshold = 50000

    # Check eligibility using conditional statements
    if customer.credit_score > credit_score_threshold and customer.annual_income >= annual_income_threshold:
        eligibility_message = "Congratulations! You are eligible for a loan."
    else:
        eligibility_message = "Sorry, you are not eligible for a loan at this time."

    return eligibility_message

# Taking input from the user
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: $"))

# Create a Customer object
customer = Customer(credit_score, annual_income)

# Checking loan eligibility and displaying the result
result_message = check_loan_eligibility(customer)
print(result_message)
