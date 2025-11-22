nums = [1,2,3,4,5,6]

def even_num(x):
    return x % 2 == 0

# Filter returns values only if the condition is true

even_numbers = list(filter(even_num, nums))
print(even_numbers) # [2, 4, 6]