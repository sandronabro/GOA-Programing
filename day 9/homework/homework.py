deposit_amount = float(input("Enter the deposit amount: $"))
interest_rate = float(input("Enter the annual interest rate: %"))

interest_rate = interest_rate / 100

amount_earned = deposit_amount * (1 + interest_rate * 2)

print("after 2 years you will have: $" + str(amount_earned))