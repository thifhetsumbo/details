# ************ Compulsory Task 2 ************

# Ask the user to enter a sentence using the input() method. Save the user’s response in a variable called str_manip.

str_manip = input("Please, briefly explain your job in one sentemce: ")

# Calculate and display the length of str_manip.

print(len(str_manip))

# Find the last letter in str_manip. Replace every occurrence of this letter in str_manip with ‘@’.

str_manip = str_manip.replace(str_manip[-1], "@")

# Print the last 3 characters in str_manip backwards.

print(str_manip[-1:-4:-1])

# Create a five-letter word that is made up of the first three characters and the last two characters in str_manip.

print("{}{}".format(str_manip[0:3], str_manip[-2:]))