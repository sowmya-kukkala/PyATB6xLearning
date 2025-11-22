numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

# Effective way to use map rather than the earlier way
square_all_numbers = list(map(square, numbers))
print(square_all_numbers) # [1, 4, 9, 16, 25]

# Earlier way
# for i in numbers:
#     print(square(i))



