# secondconverter.py
# Translate seconds into a more readable hours, minutes, and seconds


# Explains on the terminal (via the print function) what this program does.
print("Welcome to my Second Converter!")
print("This program will properly calculate the number of minutes and seconds under 60 from a given number of seconds.")

# Prompt the user to enter a number of seconds, store in a variable.
sec = int(input("How many seconds do you want to convert? "))

# Computes hours, minutes, and seconds.
s = sec  % 60
m = (sec - s) // 60 % 60
h = (sec - s) // 60 // 60

#Print the results
print(sec, "seconds is equal to", h, "hours,", m, "minutes, and", s, "seconds.")