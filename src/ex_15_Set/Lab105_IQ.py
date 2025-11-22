# Find the first non-repeating character in a string

# swiss -> s is repeating letter , w -> first non-repeating character
s = set()

def first_non_repeating_character(string):
    for char in string:
        if string.count(char) == 1:
            s.add(char)
            return char
    return None


print(first_non_repeating_character("swiss")) # w
print(first_non_repeating_character("annusinha")) # u
print(s) # {'u', 'w'}

# s = "swiss"
# print(s[0])
# print(len(s))
# print(s.count('s'))

# print(set("swiss"))



