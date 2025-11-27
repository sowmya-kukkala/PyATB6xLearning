# # Note: Pip is a package manager. At the time we install Python, pip will come along with it
# # Go to Terminal, (.venv) PS C:\Users\Sowmya\PycharmProjects\PyATB6xLearning> pip install dotenv
# # dotenv library helps to read the values from .env file

from dotenv import load_dotenv
import os

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        load_dotenv(dotenv_path=r"C:\Users\Sowmya\PycharmProjects\PyATB6xLearning\.env")
        if self.email == os.getenv("USER") and self.password == os.getenv("PASSWORD"):
            print("Allowed, Login Success")
        else:
            print("Login Failed")

email = input("Enter the vwo login email: ")
password = input("Enter the vwo login password: ")

vwo_object_ref = VWOLoginPage(email,password)
vwo_object_ref.login_confirm()

# print(os.getenv("USERNAME")) # Sowmya
print(os.name) # nt
