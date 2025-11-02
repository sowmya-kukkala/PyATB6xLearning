# Write a program to take a user age and
# let him know if he can go to the Club
# 21

# Logic Building Formula

# Step 1
# i/p - age, int
# o/p - String (result -> Can go to Club or not)

# Step 2 Rough Logic (Brute Force)
"""
age > 21 -> Print Can go
age < 21 -> Print Can't go
"""

# Step 3 Write the Logic
age = int(input("Enter the age\n").strip())

if age <=0 or age >=130:
    print("Enter a valid age")
else:
    if age>=21:
        print("Yes, can go to Club")
    else:
        print("No, can't go to Club")

# Step 4 Check for the Edge Cases
# We should consider edge cases such as :
# Negative ages or extremely high values -> Program will break
# Non-numeric input - ABC
# Age which is valid - >130

# Step 5 Optimize the Code
# Handle all the Edge cases

