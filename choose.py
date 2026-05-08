# choose.py

# Demonstrates use of a for loop to find the factorial of a number, 
# and then uses that to find the number of ways to choose k objects from a set of n distinct objects.


# Finds the factorial of the first number
n = int(input("Please give me a number: "))
product = 1
for i in range(1, n + 1):
    product = product * i

# Finds the factorial of the second number
k = int(input("Please give me a number: "))
product2 = 1
for i in range(1, k + 1):
    product2 = product2 * i

# Finds the factorial of n-k   
final = n-k
product3 = 1

for i in range(1, final + 1):
    product3 = product3 * i
    print(product3)

# Gives the final answer
finalanswer = product // (product2 * product3)
print("Your final answer is", finalanswer)