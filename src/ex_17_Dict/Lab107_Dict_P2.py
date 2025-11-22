# If duplicated key-value pair provided it keep the latest value
student_info = {
    "name": "Pramod",
    "age" : 65,
    "age" : 60,
    "address": "KA"
}

print(student_info) # {'name': 'Pramod', 'age': 60, 'address': 'KA'}
print(student_info["name"]) # Pramod
print(student_info["age"]) # 60
print(student_info["address"]) # KA
student_info["age"] = 100
print(student_info) # {'name': 'Pramod', 'age': 100, 'address': 'KA'}
