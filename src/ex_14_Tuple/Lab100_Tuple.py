shopping_list = ["bread", "butter", "paneer"]
shopping_list[2] = "milk"
print(shopping_list) # ['bread', 'butter', 'milk']

# Real case of Tuples -> If you want to do any changes to tuple. Alternatively, you can convert the tuple into list
# once the elements got modified/added later we can convert back to tuple
my_tuple = ("tta.com","sdet.live")
print(my_tuple) # ('tta.com', 'sdet.live')
my_api_list = list(my_tuple)
my_api_list.append("item2")
print(my_api_list) # ['tta.com', 'sdet.live', 'item2']
my_api_tuple = tuple(my_api_list)
print(my_api_tuple) # ('tta.com', 'sdet.live', 'item2')

# Real case where we use tuples
API_URLs = ("https://sdet.live/python0x","https://awesomeqa.com")
print(API_URLs[0]) # https://sdet.live/python0x
print(API_URLs[1]) # https://awesomeqa.com

# Creating an empty tuple
t = tuple()
print(t)  # ()

# Creating an empty list
l = list()
print(l) # []

# Conversion list to tuple
t1 = tuple(["pramod", "amit", "manisha"])
print(t1)  # ('pramod', 'amit', 'manisha')

# Combining more than one tuple
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Dianna Prince")
new_tuple = (hero1, hero2)

print(new_tuple)  # (('Batman', 'Bruce Wayne'), ('Wonder Woman', 'Dianna Prince'))

print((new_tuple)[0]) # ('Batman', 'Bruce Wayne')

print((new_tuple)[0][0])  # Batman


