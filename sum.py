# sum.py
# Computes the sum of the first n positive integers
#
# Rachel Gibson


# Asks user to input a number
n = int(input("Please give me a number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i

# Prints answer
print("The sum of the first", i, "positive integers is", sum)
