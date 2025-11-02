# Write a Python program to calculate the
# Area of a Triangle given its base and height using the formula
# area = 1/2 * base * height
# base = 10, height = 5 and print the result using arithmetic Operators

# given input type as float
# Where user enters base as 10 and height as 5

base = float(input("Enter the base of Triangle: \n"))
height = float(input("Enter the height of Triangle: \n"))
area_of_triangle = (0.5 * base * height)
print(f"Area of Triangle: {area_of_triangle:.2f}")