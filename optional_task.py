# ************ Optional Bonus Task ************ 

''' This progam reads the phrase "Merry Christmas" in reverse 
and displays it. The gives a position of a character in the phrase'''

# Define a variable phrase

phrase = "Marry Christmas"

# Display the phrase in reverse

# Logicical error

print(phrase[14:0:-1]) # The 1st character is excluded, phrase incomplete

# Give the position of the character in the phrase

# Runtime error

print(phrase.index("!")) # Character "!" is not in the phrase