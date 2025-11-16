# Create a program to sum of 3 numbers from the user input
# If user doesn't enter any number, use default as 100, 200, 300

# Logic Building

# Step 1 - I/P and O/P
# I/P - int
# O/P - int

# Step 2 - Rough Logic
# return n1+n2+n3

# Step 3 - Write Logic

# Scenario 1: Taking inputs from the user

# num1 = int(input("Enter the first number: \n"))
# num2 = int(input("Enter the second number: \n"))
# num3 = int(input("Enter the third number: \n"))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

# result = sum_of_three(num1, num2, num3) # User input
# print(result)

# Scenario 2:

# result0 = sum_of_three(30,40,50)
# print(result0) # 120

# result1 = sum_of_three()
# print(result1) # 600

# result2 = sum_of_three(n1 = 10)
# print(result2) # 510

# result3 = sum_of_three(n1 = 10, n2 = 30)
# print(result3) # 340

# result4 = sum_of_three(n1 = 10, n2 = 30, n3= 40)
# print(result4) # 80

# assigning user provided input variable to parameter
num3 = int(input("Enter the third number: \n"))

result5 = sum_of_three(n3 = num3)
print(result5) # 303













