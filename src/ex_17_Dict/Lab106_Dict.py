my_dict = {
    "name": "Aman",
    "age": 32,
    "role": "SDET",
    "exp" : 3
}

print(my_dict) # {'name': 'Aman', 'age': 32, 'role': 'SDET', 'exp': 3}

print(my_dict["age"]) # 32

print(my_dict["role"]) # SDET

# Modify the value based on the key
my_dict["role"] = "Automation Tester"
print(my_dict)  # {'name': 'Aman', 'age': 32, 'role': 'Automation Tester', 'exp': 3}

# Delete a key-value pair
del my_dict["role"]
print(my_dict)  # {'name': 'Aman', 'age': 32, 'exp': 3}

# To iterate over dictionary key, value

for key, value in my_dict.items():
    print(key, value)

# name Aman
# age 32
# exp 3

# Verfiy whether a specific key-value present in dict or not
print("age" in my_dict) # True
print("role" in my_dict) # False