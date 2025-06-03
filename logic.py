# ************ Compulsory Task 2 ************ 

''' This program asks the user to input number of days they worked, as 
well as hours they worked per day and their hourly pay rate. It 
calculates user's earnings from provided information and then 
determines if the user qualifies for commission. User only qualifies 
for commission when they have worked more than 8 hours a day. Then 
displays user's salary which is earnings and commssion. When the user 
has not qualified for commission, it displays user's salary as 
only earnings'''

# Ask the user to input number of days they worked

num_days = int(input("Please enter number of days worked: "))

# Ask the user to input hours they worked per day

hours_worked = float(input("Please enter number of hours worked per day: "))

# Ask the user to input their hourly pay rate

hourly_rate = float(input("Please enter the hourly wages: "))

# Calculate user's earnings
earnings = num_days * hours_worked * hourly_rate

# Determine if the user qualifies for commission

if hours_worked > 8:

# Calculate commission

    commision = earnings * 0.1

# Calculate salary

    salary = commision + earnings

# Display salary
    print(f"Your salary is your earnings plus commission: {salary}")

# Display salary when the user hasn't qualified for commission

    if hours_worked <= 8:
        print(f"Your salary is your earnings: {earnings}")

''' The program runs and display the salary perfectly only when the 
user has worked more than 8 hours, however when the user has worked 
less than 8 hours the salary is not displayed because the second 
condition is given under the first condition thus making it null. The 
second condition should not be indented under the 1st condition to 
determine if it's met then run independently'''