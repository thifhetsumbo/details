# ************ Compulsory Task 1 ************

''' This program creates text file that students can use to register at 
the exam venue by signing on dotted lines next to their ID numbers.'''

# Request the user to enter number of students who are registering.

num_stu = int(input("Please enter number of students registering: "))

# Stop the program if the user enters zero.

if num_stu > 0:

# Iterate for the number of students entered.

    for i in range(num_stu):

# Request the user to enter the student ID number.
        
        stu_ID = input("Please enter the student's ID: ")

# Open, create a text file for writing, appending student ID number.

        form = open('reg_form.txt', 'a')

# Count students

        c = i + 1

# Write ID numbers with student count, tab, dotted line, into text file.
# Triple space for signature, tab for clear reading, count list student.

        form.write("\n" + str(c) + ". " + stu_ID + "\t" + "........" + "\n\n")

# Move to the next student.

        i = i + 1

# Close the file

    form.close()