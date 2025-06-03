# ************ Compulsory Task ************

''' This program reads the data from the text file provided (DOB.txt) 
and prints it out in two different sections. Individual names on the 
first section and subsequent birthdates on the second section. '''

# Print the Name heading in bold

print("\n\033[1mName\033[0m")

# Open the provided file (DOB.txt)

with open("DOB.txt", "r") as file:

# Read and list all the lines in the file

    lines = file.readlines()

# Give condition to remove the \n character from each line in the list

    for line in lines:
        word = line.strip()

# Split individual words separated by space in each line into a list

        word = word.split(" ")

# Give condition to retain only the first two words in the list

        for index in range(len(word)):
            words = word[0:2]

# Join the two words into a string while separating them with space

            name = " ".join(words)

# Display all the names in separate lines

            print(name)

# End the loop to avoid further interation

            break


# Print the Birthdate heading in bold

print("\n\033[1mBirthdate\033[0m")

# Open the provided file (DOB.txt)

with open("DOB.txt", "r") as file:

# Read and list all the lines in the file

    lines = file.readlines()

# Give condition to remove the \n character from each line in the list

    for line in lines:
        word = line.strip()

# Split individual words separated by space in each line into a list

        word = word.split(" ")

# Give condition to retain only the third word upto the last in the list

        for index in range(len(word)):
            words = word[2:]

# Join the two words into a string while separating them with space

            birthdate = " ".join(words)

# Display all the birthdate in separate lines

            print(birthdate)

# End the loop to avoid further interation

            break