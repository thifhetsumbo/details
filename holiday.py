# ************ Compulsory Task 1 ************

''' This program calculates the user’s holiday cost using plane cost, 
hotel cost, and car rental cost. '''

''' Request the user to enter the city code they are flying to. JHB for 
 Johannesburg, DBN for Durban and CPT for Cape Town.'''
city_flight = input("Enter destination city code (JHB, DBN, CPT): ").upper()

# Make sure user input city is part of the airline route.
while city_flight not in ["JHB", "DBN", "CPT"]:
# Let user know that city of their choice is not part of airline routes.
    print("Chosen city not part of airline routes.")
    # Request the user to enter the city they are flying to again.
    city_flight = input("Enter destination city code (JHB, DBN, CPT):").upper()

# Request user to enter number of nights they'll be staying at a hotel.
num_nights = int(input("Enter number of nights to be spent at a hotel: "))

# Request user to enter number of days they will be hiring a car for.
rental_days = int(input("Enter number of days you’ll be hiring a car for: "))

# Define a function to calculate total hotel cost.
def hotel_cost(x, num_nights):
    total_hotel_cost = x * num_nights
    return(total_hotel_cost)

# Define a function to assign flight cost.
def plane_cost(city_flight):
    if city_flight == "JHB":
        total_plane_cost = 1500
    elif city_flight == "DBN":
        total_plane_cost = 1000
    elif city_flight == "CPT":
        total_plane_cost = 1200
    return(total_plane_cost)

# Define a function to calculate total car rental cost.
def car_rental(x, rental_days):
    total_car_rental = x * rental_days
    return(total_car_rental)

# Calculate hotel, flight, car rental cost using above defined function.
hotel_amount = hotel_cost(950, num_nights)
plane_amount = plane_cost(city_flight)
car_rental_amount = car_rental(850, rental_days)

# Calculate the total holiday cost.
def holiday_cost(hotel_amount, plane_amount, car_rental_amount):
    total_holiday_cost = hotel_amount + plane_amount + car_rental_amount
    return(total_holiday_cost)
    
holiday_cost_amount = holiday_cost(hotel_amount, plane_amount, car_rental_amount)

# Assign and display heading for total holiday cost.
print("\n\033[1mTotal Holiday Cost.\033[0m")

# Display the total hotel cost.
print(f"Total Hotel Cost: R {hotel_amount:.2f}")

# Display the total plane cost.
print(f"Total Plane Cost: R {plane_amount:.2f}")

# Display the total car rental cost.
print(f"Total Car Rental Cost: R {car_rental_amount:.2f}")

# Display the total holiday cost.
print(f"Total Holiday Cost: R {holiday_cost_amount:.2f}")
