a = {1,2,3}
b = {3,4,5}

print(a|b)      # {1, 2, 3, 4, 5}
print(a.union(b))   # same result

print(a & b)    # {3}
print(a.intersection(b)) # same result

print(a.difference(b)) # {1, 2}
print(a - b) # same results - returns elements in 'a' but not in 'b' and common elements

print(b - a)   # {4, 5} # returns elements in 'b' but not in 'a' and common elements

print(a.symmetric_difference(b))  # {1, 2, 4, 5} # Displays the values that are not common in both the sets
print(a ^ b)  # returns the same results

set1 = {1, 2, 3}
set2 = {4, 5, 6}

my_set = set1.union(set2)
print(my_set)       # {1, 2, 3, 4, 5, 6}

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
my_set = set1.intersection(set2)
print(my_set)       # {4, 5}

my_set = set1.difference(set2)
print(my_set) # {1, 2, 3}

my_set = set2.difference(set1)
print(my_set)  # {8, 6, 7}
