# fibonacci.py
# This programs computes the nth Fibonacci number!

print("My incredible Fibonacci number generator!")

# Asks user for a number.
n = int(input("Please give me an integer: "))

# Sets current and previous numbers.
previous = 1
current = 1

#Computes the Fibonacci sequence.
for i in range(0, n):
    previous = current - previous
    current = current + previous

print("The ", n, "th number in the Fibonacci sequence is ", current - previous, ".", sep='', end='')
print()