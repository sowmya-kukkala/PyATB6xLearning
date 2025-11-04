# Question 2 :
# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.
# Hint: Use a while loop with a counter.
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed

number_of_retry_attempts=0
while number_of_retry_attempts <=2 :
    response_code = int(input("Enter the response code:\t").strip())
    if response_code == 200:
        print("✅ Test Passed")
        break
    elif response_code != 200:
        print("Retry the response")
    number_of_retry_attempts = number_of_retry_attempts + 1
else:
    print("Test Failed")




