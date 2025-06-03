# ************ Compulsory Task 1 ************

''' This program requests a user to enter instructions to the learners 
and then makes each alternate character an uppercase and each other 
alternate character a lowercase. It also requests the user to enter a 
favourite quote and then make each alternate word an uppercase and each 
other alternate word a lowercase. Lastly, it displays the instructions 
to the leaners and user’s favourite quote in a new format.'''

# Requests the user to enter instructions to the learners

instruction = input("Please enter an instruction to the learners: ")

# Assign a variable to the final instructions to be diplayed

final_instruction = ""

''' Give conditions to make even characters uppercase and odd 
characters lowercase while keeping them as a single string '''

for i in range(len(instruction)):
    if i % 2 == 0:
        final_instruction += instruction[i].upper()
    else:
        final_instruction += instruction[i].lower()

# Requests the user to enter their favourite quote

quote = input("Please enter your favourite quote: ")

# Split the quote into a lsit of words

split_quote = quote.split()

''' Assign a variable to the list where all words which were splitted 
from the quote will be stored after changing the case of the words'''

list_quote = []

''' Give conditions to make words with odd index uppercase and those 
with even index lowercase while keeping them in one list '''

for index in range(len(split_quote)):
    if index % 2 == 1:
        list_quote.append(split_quote[index].upper())
    else:
        list_quote.append(split_quote[index].lower())

# Join all the words in the list into a sentence

favourite_quote = " ".join(list_quote)

# Display the instructions to the leaners with a new format

print(f"The final instruction to the learners is \"{final_instruction}\"")

# Display the user’s favourite quote with a new format

print(f"Your favourite quote is \"{favourite_quote}\"")