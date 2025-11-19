# SET
# Collection of Unique elements
# {} - Parenthesis
# immutable/value can be modified
# non-ordered collection
# heterogenous

list_of_unique_items = {1,2,3,4,4,5,5}
print(list_of_unique_items)  # {1, 2, 3, 4, 5}

list1 = [45.2, 33, 33, 45, 21]
set1 = set(list1)
print(set1)  # {33, 21, 45, 45.2}

t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(t)
print(set(t)) # {'for', 'TheTestingAcademy'}

# Here set considers True as 1 
mixed = {1, "QA", True, 3.5}
print(mixed) # {1, 3.5, 'QA'}

empty = set()
print(empty) # set()
print(type(empty))  # <class 'set'>

# Read all the items from the set
for item in mixed:
    print(item)

# 1
# 3.5
# QA

# Add values to the set
mixed.add(10)
print(mixed)  # {'QA', 10, 3.5, 1}

# Remove values from the set
mixed.remove(10)
print(mixed) # {1, 3.5, 'QA'}

mixed = {1, "QA", True, False, 3.5}
print(mixed)  # {False, 1, 'QA', 3.5}




