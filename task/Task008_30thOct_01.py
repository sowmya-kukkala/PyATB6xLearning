# Q: Create a function which will take a positive number from the user and perform square of the number?

# i/o = 3
# o/p = 9

def square_of_num(num):
    return num ** 2

input_num = int(input("Enter a number to be squared: ").strip())
print("Square of number",input_num, " is ",square_of_num(input_num))