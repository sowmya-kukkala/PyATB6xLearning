# 🧩 1️⃣ Write a Function to Check Test Case Status
# Problem:
# Write a function check_status(status_code) that returns:
# "PASS" if status_code = 200
# "FAIL" if status_code = 400 or 500
# "UNKNOWN" otherwise
from unittest import case


# Example Input & Output:
# print(check_status(200))   # PASS
# print(check_status(500))   # FAIL
# print(check_status(302))   # UNKNOWN

# Defining a function
def check_test_case_status(status_code):
    match status_code:
        case 200:
            return "PASS"
        case 400:
            return "FAIL"
        case 500:
            return "FAIL"
        case _:
            return "UNKNOWN"

# Inputs from the user for status code
status_code = int(input("Enter a status code: "))

# Calling the function
print(check_test_case_status(status_code))


print(check_test_case_status(200))
print(check_test_case_status(400))
print(check_test_case_status(500))
print(check_test_case_status(302))

