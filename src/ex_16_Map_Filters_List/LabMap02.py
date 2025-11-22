name = ["Pramod", "lucky", "tester"]

def string_in_upper_case(string):
    return string.upper()

# Note: Map generally works with single parameter

strings_in_upper = list(map(string_in_upper_case, name))
print(strings_in_upper) # ['PRAMOD', 'LUCKY', 'TESTER']