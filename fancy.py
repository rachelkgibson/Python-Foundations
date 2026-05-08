# fancy.py
# A fancy greeting program that demonstrates the use of the input function and string concatenation in a print statement.

# Asks user for their first name
firstname = input("Enter your name: ")

# Asks user for their nickname
nickname = input("Enter your nickname: ")

# Ask user for their last name
lastname = input("Enter your last name: ")

# Prints greeting
print("Welcome back, ", firstname, " \"", nickname,"\" ",lastname, "!", sep='')
