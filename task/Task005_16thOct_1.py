# Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.

response_code = int(input("Enter your response code: ").strip())

if response_code == 200:
    print("✅ Passed API Request")
else:
    print("❌ Failed API Request")
