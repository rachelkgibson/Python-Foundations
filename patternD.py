# patternD.py
# Prints a pattern variation of patternA.py.



# Asks user for a number.
n = int(input("Please enter an integer: "))
#Prints the nested for loop.
for i in range(1, n+1):
    for k in range (1, i+1):
        for j in range(1, k+1):
             print(k, end=' ')
    print()

