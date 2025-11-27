class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if (self.email == "pramod@gmail.com" and self.password == "pass123"):
            print("Allowed, Login Success")
        else:
            print("Login Failed")

# email = # Read from test data - Excel, CSV or env file
# password = # Read from test data - Excel, CSV or env file

# vwo_object_ref = VWOLoginPage(email, password)
# vwo_object_ref.login_confirm()

pramod = VWOLoginPage("pramod@gmail.com", "pass123")
pramod.login_confirm()