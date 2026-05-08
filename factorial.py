# factorial.py
# Computes the product of the first n positive integers.

# Asks user to input number
n = int(input("Please give me a number: "))
product = 1
for i in range(1, n + 1):
    product = product * i

# Prints the answer
print("The factorial of the first", i, "positive integers is", product)