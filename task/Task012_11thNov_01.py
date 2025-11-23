# Question - ✅ Count vowels and consonants in a String

input_string = input("Enter a string: ") # automation

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in input_string:
    if char in vowels:
        vowel_count +=1
    else:
        consonant_count +=1

print("The vowel count in ",input_string, "is: ", vowel_count)
print("The consonant count in ",input_string, "is: ", consonant_count)

