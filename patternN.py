# patternN.py
# Prints an N star pattern.

# Asks user for a number.
n = int(input("Please enter an integer: "))

# Prints the top part of N.
print("*", end=' ')
for i in range(1, n):
    print(" ", end='')
print("*", end=' ')
print()

# Prints the middle part of N.
for i in range(0, n):
    print("*", end='')
    print(i*" ",end='')
    print("*", end='')
    print(" "*(n-i-1), end='')
    print("*")

# Prints the middle part of N.
print("*", end=' ')
for i in range(1, n):
    print(" ", end='')
print("*", end=' ')
print()