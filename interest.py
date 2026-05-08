# interest.py
# Calculates the total interest accrues on your initial deposit to the bank.

print("Welcome to the Interest Calculator!")

# Asks user for initial savings.
initial_savings = int(input("Enter your initial savings: "))

# Asks user for monthly interest rate.
interest_rate = float(input("Enter the monthly interest rate: "))

# Asks user for monthly contribution.
monthly_contribution = int(input("Enter your monthly contribution: "))

# Asks user for how many months will be computed.
months_computed = int(input("How many months would you like computed: "))

# Prints the initial value.
print("Initially you put in ", "$", initial_savings, sep='')

# Computes the total for each month.
savings = initial_savings
for i in range(1, months_computed + 1):
    savings = savings + (savings*interest_rate) + 20
    savings = (savings * 100)
    savings = int(savings)
    savings = savings / 100
    print("After month ", i, " you would have ", "$", savings, sep='')
