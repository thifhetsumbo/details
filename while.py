# ************ Compulsory Task 1 ************

''' This program asks the user to enter a number repeatedly unitl the
 user enters -1, then the program stops requesting the user to enter
 a number and calculates the average of the numbers entered, excluding
 the -1 entered last'''

# Assign a variable to a list of numbers

num_list = [] # Using list so to append input number when entered

# State the condition to be met and statement to be executed

while True:

# Using float to accomodate decimal numbers

    num_input = float(input("Please enter a number, not -1 (-1 to stop): "))
    if num_input == -1: # Stop the loop if user entered -1
        break

# Add each entered number satisfying the condition to list of numbers

    num_list.append(num_input)

# Take the average of one or more numbers entered, else stop

if len(num_list) > 0:
    average_num_list = sum(num_list) / len(num_list)

# Print the list of numbers that met the condition

    print(f"Input numbers: {num_list}")

# Print the average of numbers that met the condition

    print(f"Average of input numbers per count (excluding -1): {average_num_list}")







