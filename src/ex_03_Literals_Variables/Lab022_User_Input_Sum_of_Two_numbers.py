# Write a program to take 2 user input numbers then
# Sum the numbers
# Multiply the numbers
# Division the numbers

# Logic Building

#Step1:
#I/P -> num1, num2 -> int
#O/P -> sum, mul, div (data type of the output - Always ask from the interviewer). Now given, float

# Note: If the input type is int or decimal, float will accept all. Hence, we chose float type to define the input type

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(num1+num2)
print(num1*num2)
print(num1/num2)