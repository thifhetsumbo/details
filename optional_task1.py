# ************ Optional Bonus Task 1 ************

# Ask the user to enter the lengths of all three sides of a triangle.

side1 = float(input("Please enter the length of a 1st side of a triangle: ")) # Using float in case the lenghths of the sides of a triangle are in decimal numbers 
side2 = float(input("Please enter the length of a 2nd side of a triangle: "))
side3 = float(input("Please enter the length of a 3rd side of a triangle: "))

#Calculate the area of the triangle.

s = (side1 + side2 + side3) / 2
print(s)
import math
area_triangle = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

# Print out the area.

print("Area of a tringle is: {}".format(area_triangle))