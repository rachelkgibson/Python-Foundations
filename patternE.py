# patternE.py
# Prints an E star pattern.

# Asks user for a number.
n = int(input("Please enter an integer: "))

#Prints the nested loop.
for i in range(0, n+2):
    print("*", end='')
print()
for i in range(0, n):
    print("*")
for i in range(0, (n+2)-1):
    print("*", end='')
print()
for i in range(0, n):
    print("*")
for i in range(0, n+2):
    print("*", end='')
print()

    
    
  
            

        

   