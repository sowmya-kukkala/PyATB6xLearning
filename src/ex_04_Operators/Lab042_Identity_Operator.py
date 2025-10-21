x = [10,  20, 30]
z = [10,  20, 30]
print(x is z) # False - Since the location is different

x = [10, 20, 30]
z = x
print(x is z) # True
