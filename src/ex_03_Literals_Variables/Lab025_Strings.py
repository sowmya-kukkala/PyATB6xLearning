name = "This is a Big Line"
print(type(name))

# name = name+1
# print(name) # TypeError: can only concatenate str (not "int") to str

name = name+str(1)
print(name) # This is a Big Line1

fname = "Pramod"
lname = "Datta"
fullname = fname+" "+lname
print(fullname) # Pramod Datta
print(type(fullname)) # <class 'str'>