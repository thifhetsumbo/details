# ************ Practical Task ************

'''' This program determines the award a person competing in a
triathlon will receive. It reads the time (in minutes) for all three
events of a triathlon, namely swimming, cycling, and running, and then
calculates and displays the total time taken to complete the triathlon,
as well as the award that the participant will receive.'''

# Ask user to enter time (in minutes) taken to complete swimming race.

swim_time = int(input("Please enter time taken to swim: "))

# Ask user to enter time (in minutes) taken to complete cycling race.

cycle_time = int(input("Please enter time taken to cycle: "))

# Reads the time (in minutes) taken to complete running race.

run_time = int(input("Please enter time taken to run: "))

# Calculate and display the total time taken to complete the triathlon.

triathlon_time = swim_time + cycle_time + run_time
print(triathlon_time)

# Displays the award that the participant will receive.

if triathlon_time <= 100:
    print("Qualified within 0-100 minutes, awarded Provincial colours.")
elif triathlon_time >= 101 and triathlon_time <= 105:
    print("Qualified within 101-105 minutes, awarded Provincial half colours.")
elif triathlon_time >= 106 and triathlon_time <= 110:
    print("Qualified within 106-110 minutes, awarded Provincial scroll.")
else:
    print("Qualified with more than 110 minutes, thus no award.")