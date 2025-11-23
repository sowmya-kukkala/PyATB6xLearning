# 🧩 Example Walkthrough
# Let’s take the word "level":
# Forward: "level"
# Backward: "level"
# Both are identical → Palindrome ✅
# Now, "hello":
# Forward: "hello"
# Backward: "olleh"
# Not the same → Not a palindrome ❌

input_string = input("Enter a string: ")

actual_string = input_string

def reverse_string(input):
    reverse = input[::-1].lower()
    return reverse

expected_string = reverse_string(input_string)

if expected_string == input_string:
    print(actual_string, "is Palindrome ✅")
else:
    print(actual_string, "is not a palindrome ❌")




