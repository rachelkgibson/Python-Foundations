# patternB.py
# Prints a pattern variation of patternA.py that includes all numbers from 1 to n.



# Asks user for a number.
n = int(input("Please enter an integer: "))

#Prints the nested for loop.
for i in range(1, n+1):
  
    for j in range(1, n+1):
        print(i, end=' ')
    print()