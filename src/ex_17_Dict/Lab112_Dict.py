dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1.keys()) # dict_keys(['a', 'b', 'c'])
print(dict1.values()) # dict_values([1, 2, 3])

dict2 = {"a": 1, "b": 2}

# missing_keys = dict1 - dict2 # TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
# print(missing_keys)

missing_keys = set(dict1.keys() - dict2.keys()) # Applied set to avoid duplicates
print(missing_keys) # {'c'}