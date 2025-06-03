# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

''' Lion is a string, therefore it should be in "". This is a 
syntaxis error '''

animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

''' Use f-string to convert number_of_teeth variable interger value to 
a string and add string variables, animal, animal_type and 
number_of_teeth together. Swap the locations of number_teeth with 
animal_type. This is a logical error'''

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

''' Add missing paranthesis and remove space after print. This is a 
sytanxis error.'''

print(full_spec)