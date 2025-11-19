# List values can be modified

my_list = [1, 2, 3]
my_list[0] = "sample"
my_list[2] = "test"

# print(my_list) # ['sample', 2, 'test']

for item in my_list:
    print(item)

# sample
# 2
# test

# Note: range() also returns the list
for i in range(1,5):
    print(i)

# 1
# 2
# 3
# 4

# range() is a function which creates a list and returns that

my_list = [1, 2, 3]
# Indexing
print("element at the index 0 is: ", my_list[0])
print("element at the index 1 is: ", my_list[1])
print("element at the index 2 is: ", my_list[2])

# element at the index 0 is:  1
# element at the index 1 is:  2
# element at the index 2 is:  3

# append() - append the value/object to the end of the list
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

my_list.append(5)
print(my_list) # [1, 2, 3, 4, 5]

# extend() - append a new list
my_list.extend([7,8,9,10])
print(my_list)  # [1, 2, 3, 4, 5, 7, 8, 9, 10]

# insert() - to add the value at particular index
my_list.insert(1, "Dutta")
print(my_list)  # [1, 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]
print(len(my_list)) # 10

my_list.insert(0, 0)
print(my_list) # [0, 1, 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]

my_list[1] = "Amit"
print(my_list)  # [0, 'Amit', 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]

# remove() - to remove the value directly
my_list.remove("Amit")
print(my_list)  # [0, 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]

# copy() - to create a copy of the list

my_copy_list = my_list.copy()
print(my_copy_list)  # [0, 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]

my_copy_list.remove("Dutta")
print(my_copy_list)  # [0, 2, 3, 4, 5, 7, 8, 9, 10]

print(my_list) # [0, 'Dutta', 2, 3, 4, 5, 7, 8, 9, 10]



