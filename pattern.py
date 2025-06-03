'''' This code outputs the star pattern which start with one star,
 increases by one star on each new line until five stars where it
 starts decreasing with one star until only one star is left'''

# Set a variable for the stars variable

stars = "*"

# Set a range for a total number of stars and set character variable

for i in range(0 , 5):

# Display stars for the whole range on each line

    print(stars)

# Add each star and then run the loop again if conditions are stil met

    stars = stars + "*"

# Start with four stars to decrease them by one on each line

else:
    stars = "****"

# Set a range for number of stars and set character variable

    for i in range(0 , 4):

# Decrease number of stars by one on each line

                index = 4 - i

# Display stars for the whole range on each line

                print(stars[0:index])