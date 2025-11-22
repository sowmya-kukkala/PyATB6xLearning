# squares = { x ** 2 for x in range(5)}
# print(squares) # {0, 1, 4, 9, 16}

# Ideal way to use the for loop mostly by avoiding the single liner as follows

squares = []
squares_set = {}

for x in range(5):
    squares.append(x**2)
    squares_set = set(squares)

print(squares)  #[0, 1, 4, 9, 16]
print(squares_set) # {0, 1, 4, 9, 16}

# Frozen set (Immutable Set)
# A Frozen set cannot be hanged after creation - Picks only unique values and no duplication as well

fset = frozenset([1, 2, 3, 3])
print(fset) # frozenset({1, 2, 3})
print(type(fset)) # <class 'frozenset'>



