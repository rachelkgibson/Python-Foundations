# sequence.py
# Lists the squares of all integers from a start number down to one.

# Asks user for a number.
start = int(input("Please give me a number: "))

# Counts down by squares from the start number to 1.
for start in range(start, 0, -1):
    start = start * start
    if start == 1:
        print(start)
    else:
        print(start, ", ", sep='', end='')

