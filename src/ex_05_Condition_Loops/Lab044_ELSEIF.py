# Find the positive number is Ever or Odd

num = int(input("Enter a number: ").strip())

# Method 1
"""
if num > 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative Number")
"""

# Method 2 - You can write short one-liner conditions using Ternary Operator
if num > 0:
    print("Even" if num %2==0 else "Odd")
else:
    print("Negative Number")