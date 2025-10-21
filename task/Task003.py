# Write a Python program to calculate the
# Area of a Circle given its radius using the formula
# area = pi * r^2 (Take pie as 3.14)
import math

# given input - r is of float type
# output -> String formatted output of area

# Logic Building Formula
# || Step - 1 ||
# Figure out the inputs and output
# input -> r -> data type -> float
# output -> String -> float - area, print area

# || Step - 2 ||
# rough logic = area = 3.14 * pow(r,2)

# || Step - 3 ||
radius = float(input("Enter radius of the circle:\n"))
# area_of_circle = 3.14 * (radius ** 2)
# area_of_circle = 3.14 * pow(radius,2)
area_of_circle = math.pi * pow(radius,2)

print("The Area of circle is: ", area_of_circle)

# String data formatting (or) Python f-strings (or) formatted String literals
print(f"The Area of circle is -> {area_of_circle:.2f}")
