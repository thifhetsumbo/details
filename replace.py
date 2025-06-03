# ************ Compulsory Task 1 ************

# Please save the following sentence as a single string: "The!quick!brown!fox!jumps!over!the!lazy!dog."

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Reprint this sentence as “The quick brown fox jumps over the lazy dog.” Using the replace() function to replace every “!” exclamation mark with a blank space.

sentence = sentence.replace("!", " ")
print(f"sentence.replace(): {sentence}")

# Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.” Using the upper() function.

sentence = sentence.upper()
print(f"sentence.upper(): {sentence}")

# Print the sentence in reverse.

print(sentence[::-1])