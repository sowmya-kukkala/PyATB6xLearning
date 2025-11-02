# Check if the user can log in based on correct username and password.
# I/p
# username = "admin"
# password = "1234"
# O/p
# ✅ Login Successful
# For the Fail condition Other O/P = ❌ Invalid Credentials

username_input = input("Enter username:\t")
username_expected = "admin"
password_input = input("Enter password:\t")
password_expected = "1234"

if username_input.lower().strip() == username_expected and password_input.lower().strip() == password_expected:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")
