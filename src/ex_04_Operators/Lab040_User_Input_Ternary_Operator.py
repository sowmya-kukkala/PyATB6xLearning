user_age = int(input("Enter your age: \n"))

'''
if user_age >= 18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")
'''

print("You are eligible for vote" if (user_age >= 18) else "You are not eligible for vote")
