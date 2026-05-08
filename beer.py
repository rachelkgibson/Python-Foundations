# beer.py
# Prints the whole "99 Bottles of Beer on the Wall" song using a for loop.



# Shows the number of beers. Counts down by 1 from 99 and ends at 0.
for NUM_BOTTLES in range (10, 0, -1):
    print(NUM_BOTTLES, "bottles of beer on the wall")
    print(NUM_BOTTLES, "bottles of beer!")
    print("Take one down, pass it around")
    print(NUM_BOTTLES - 1, "bottles of beer on the wall!")
    print()