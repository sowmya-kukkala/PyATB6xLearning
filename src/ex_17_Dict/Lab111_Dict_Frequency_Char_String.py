#Frequency of characters in a string

# i.e., Write a program to count the frequency of each character in a given String

# string1 = "automation"
string_input = input("Enter the input e.g. automation:  ")

# Output -> {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}

char_count = {}
for char in string_input:
    # print(char)
    char_count[char] = char_count.get(char, 0)+1

print(char_count) # {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}