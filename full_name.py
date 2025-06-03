# ************ Compulsory Task 1 ************

# This program will be used to validate that a user inputs at least two names when asked to enter their full name.

# Ask the user to input their full name.

user_nam = input("Please enter your full name i.e name and surname: ")

# Check that the user has entered a full name.

if len(user_nam) == 0:
    print("You haven’t entered anything. Please enter your full name.") # If the user did not enter display the error "You haven’t entered anything. Please enter your full name."
elif len(user_nam) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.") # If the user didn't enter their name in full display the error "You have entered less than 4 characters. Please make sure that you have entered your name and surname."
elif len(user_nam) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.") # "You have entered more than 25 characters. Please make sure that you have only entered your full name."
else:
    print("Thank you for entering your name.")