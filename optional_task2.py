# ************ Optional Bonus Task 2 ************

# Ask the name of a user's favourite restaurant and store it in a variable called string_fav.

string_fav = input("Please enter your favourite resturant: ")

# Ask the user's favourite number and use casting to store it in an integer variable called int_fav.

int_fav = int(input("Please enter your favourite number: "))

# Print out both of these using two separate print statements below what you have written.

print(string_fav)
print(int_fav)

# Cast string_fav to an integer.

string_fav = int(string_fav)

# Add a comment in your code to explain why this is.

# string_fav is a string with letters and not numbers, therefore is cannot be casted into an integer. Only strings with numbers as characters can be casted into intergers.