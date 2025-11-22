# Count the vowels in the given string

# {'a': 0, 'e':1, 'i': 0, 'o': 2, 'u': 0}

input_string = input("Enter the input string:  ") # "Hello, world!"

vowels = "aeiou"
vowel_count = {}

for char in input_string.lower():
    if char in vowels:
        vowel_count[char] = vowel_count.get(char,0)+1

print(vowel_count) # {'e': 1, 'o': 2}








