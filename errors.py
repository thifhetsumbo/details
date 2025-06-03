# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

''' Add missing paranthesis and remove space after print. This is a 
sytanxis error'''

print("Welcome to the error program")

''' Remove spaces before print to fix indentation error, remove space 
after print and add paranthesis. This is a syntaxis error'''

print("\n")

    # Variables declaring the user's age, casting the str to an int, and printing the result

''' Remove spaces before defining the variable age_string and age, to 
fix indentation error. This is a syntaxis error. Remove 
age_string == "24 years old" as it cannot be concanated, thus 
arithmetics cannot be conducted. Define the variable age as an integer 
that can easily be concatenated, this is a runtime error'''

age = 24

''' Remove space before print to fix indentation error. Concatenate 
variable age into a string, this is a runtime error. Add space after 
string "I'm" and before string "years old.", this is a logical error'''

print("I'm" + " " + str(age) + " " + "years old.")

    # Variables declaring additional years and printing the total years of age

''' Remove spaces before defining variable year_from_now and 
total_years to fix indentation error. Remove "" to change the value for 
years_from_now from a string to an interger. This is a syntaxis error'''

years_from_now = 3
total_years = age + years_from_now

''' Add missing paranthesis and remove space after print. This is a 
sytanxis error. Add a space after colons. This is a logical error'''

# This seems like a useless line to the code

print("The total number of years:" + " " + "answer_years")

# Variable to calculate the total amount of months from the total amount of years and printing the result

'''The variable total is not defined, should be using total_years. 
This is a syntaxis error'''

total_months = total_years * 12

''' Add missing paranthesis and remove space after print. This is a 
sytanxis error. Add 6 months onto total_months, this is a logical 
error. Concatenate the "total_months + 6 months" value into a string. 
This is a runtime error'''

print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")

#HINT, 330 months is the correct answer