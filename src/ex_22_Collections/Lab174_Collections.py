from collections import *

# Collections contain multiple modules

# Using Counter module

# user_input = input("Enter a string: ") # aabcbbcc
# count_char = Counter(user_input)
# print(count_char) # Counter({'b': 3, 'c': 3, 'a': 2})

# Earlier defining Tuple

# info = ("Promo", 34, True, 9.8)
# print(info) # ('Promo', 34, True, 9.8)

# Using namedTuple

info = namedtuple('info', ['name', 'age', 'graduated', 'grade'])
t = info("Promo", 34, True, 9.8)

print(t.name) # Promo
print(t.age) # 34
print(t.graduated) # True
print(t.grade) # 9.8

