# Question 2 :
# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed

# Counter for Attempts
attempt = 1
max_attempts = 3
while attempt <= max_attempts:
    response = int(input("Please enter your API response: ").strip())
    print("Attempt ", attempt, ": Response ", response)
    if response == 200:
        print("✅ Test Passed")
        break
    attempt += 1
else:
    print("❌ API call failed after 3 attempts")


