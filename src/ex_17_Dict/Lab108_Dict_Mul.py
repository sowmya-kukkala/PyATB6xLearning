student_info1 = {
    "name": "Pramod",
    "age" : 67,
    "address": {
        "home_address": "ND",
        "office_address": "KA"
    }
}

student_info2 = {
    "name": "Amit",
    "age" : 69,
    "address": {
        "home_address": "GOA",
        "office_address": "KA"
    }
}

student_info3 = {
    "name": "Murthy",
    "age" : 70,
    "address": {
        "home_address": "PODI",
        "office_address": "VZG"
    }
}

# students_list = [student_info1, student_info2]
# print(students_list)

students_list = [student_info1, student_info2, student_info3]
print(students_list)

# [{'name': 'Pramod', 'age': 67, 'address': {'home_address': 'ND', 'office_address': 'KA'}},
# {'name': 'Amit', 'age': 69, 'address': {'home_address': 'GOA', 'office_address': 'KA'}},
# {'name': 'Murthy', 'age': 70, 'address': {'home_address': 'PODI', 'office_address': 'VZG'}}]

# print(students_list[0]) # {'name': 'Pramod', 'age': 67, 'address': {'home_address': 'ND', 'office_address': 'KA'}}
# print(students_list[0]["name"]) # Pramod
# print(students_list[1]["address"]["office_address"]) # KA

print(students_list[2]["address"]["office_address"]) # VZG