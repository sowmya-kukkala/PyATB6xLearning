# List - Collection of Items
# Grocery List - Butter, Bread, Banana, Paneer
# 10th marks - 90, 91, 92, 78, 56

my_list = [1, 2, 3] # Same type of data (int)
my_list2 = [1, True, "Pramod", 12.34] # accepts different types of data (Heterogeneous)

print(my_list) # [1, 2, 3]
print(type(my_list)) # <class 'list'>
print(len(my_list)) # 3
print(my_list2) # [1, True, 'Pramod', 12.34]

# List index starts from 0
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3]) # IndexError: list index out of range