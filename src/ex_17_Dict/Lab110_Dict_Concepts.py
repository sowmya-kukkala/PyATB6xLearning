keys = ["name", "role", "experience"]
values = ["Aman", "SDET", 3]

# Converting Lists to Dictionary
my_dict = dict(zip(keys, values))
print(my_dict) # {'name': 'Aman', 'role': 'SDET', 'experience': 3}

# Merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1 | dict2
print(merged_dict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(merged_dict.get('a')) # 1

# Giving key but not value
keys = ["name", "role", "experience","abc"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values))
print(my_dict) # {'name': 'Aman', 'role': 'SDET', 'experience': 3}