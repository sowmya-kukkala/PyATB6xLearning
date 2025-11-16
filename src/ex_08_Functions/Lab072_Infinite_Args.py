def print_mul_args(*args):
    # args refers to list
    for i in args:
        print(i)

# We can define the multiple args name as below based on our choice
# def print_mul_args(*check_values):
#     # args refers to list
#     for i in args:
#         print(i)

print_mul_args("Pramod")
print("**********")
print_mul_args("Pramod", "dutta")
print("**********")
print_mul_args("Pramod", "dutta", "third")
print("**********")
print_mul_args("Pramod", "dutta", "third", 3.14)
print("**********")
print_mul_args("Pramod", "dutta", "third", 3.14, True)
print("**********")
print_mul_args(1,2,3,4,5,6)