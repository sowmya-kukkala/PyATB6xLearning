class BaseTest:
    def run(self):
        print("Running Generic Test")

class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")

# Scenario 1: Method Overriding
# t = LoginTest()
# t.run() # Running Login Test

# Scenario 2: Direct call of Method from Base Class
t = BaseTest()
t.run() # Running Generic Test