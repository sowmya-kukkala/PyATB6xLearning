# Function that returns the maximum value of dictionary and key of dictionary
# {"a": 10, "b": 20, "c": 30}

dict1 = {"a": 10, "b": 20, "c": 30}
# print(dict1.keys())
# print(max(dict1.values()))

def max_dict_value(dict):
    return max(dict.values())

def max_dict_key(dict):
    return max(dict.keys())

def min_dict_value(dict):
    return min(dict.values())

def min_dict_key(dict):
    return min(dict.keys())

print(max_dict_value(dict1)) # 30

print(max_dict_key(dict1)) # c

print(min_dict_value(dict1)) # 10

print(min_dict_key(dict1)) # a

