# Removes and returns element at the given index (default: last element)

squares = [1,4,9,16,25]
print(squares.pop()) # 25
print(squares) # [1, 4, 9, 16]

# To remove the element at particular index
print(squares.pop(1)) # 4
print(squares) # [1, 9, 16]

# clear() - removes all the elements from the list
squares.clear()
print(squares) # []

# index(element, start, end)
# Returns the index of the first occurrence of the element
numbers =  [10, 20, 30, 20, 40]
print(numbers.index(20)) # 1

print(numbers.index(20,2,4)) # 3

# count() - returns the total count of element in the list
print(numbers.count(20)) # 2

# sort() - returns the list in ascending order
numbers.sort()
print(numbers) # [10, 20, 20, 30, 40]

# sort(reverse=true) - returns the list in descending order
numbers.sort(reverse=True)
print(numbers)  # [40, 30, 20, 20, 10]

# reverse() - returns the list in reverse order
numbers.reverse()
print(numbers) # [10, 20, 20, 30, 40]

# max(), min(), sum() works for numerical lists

print(max(numbers)) # 40
print(min(numbers)) # 10
print(sum(numbers))  # 120

# Slicing
print(numbers)  # [10, 20, 20, 30, 40]
print(numbers[1:4]) # [20, 20, 30] # returns the values from Start index and end - 1 index values # from 1 to 3
print(numbers[-1]) # 40 # returns last element
print(numbers[2:-1]) # [20, 30] # from 2 to 3

print("apple" in numbers)  # False
print(20 in numbers) # True

# List Creation and Comprehension
# range(1,5) --> returns the list

l = list(range(1,5))
print(l) # [1, 2, 3, 4]

# Nested Lists
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2]) # 6

# del - deletes an element by index or the whole list
del numbers[0]
print(numbers) # [20, 20, 30, 40]



