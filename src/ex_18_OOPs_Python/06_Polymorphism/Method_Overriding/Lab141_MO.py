class TestSuite:
    def info(self):
        print("Test Suite Information")

class BaseTest(TestSuite):
    def setup(self):
        print("Base Setup")

    def run(self):
        print("Base Test Execution")

class LoginTest(BaseTest):
    def run(self): # Overriding
        print("Login Test Execution")

class APITest(BaseTest):
    def run(self): # Overriding
        print("API Test Execution")

t = LoginTest()
t.run() # Login Test Execution

t = APITest()
t.run()  # API Test Execution

t = BaseTest()
t.run()  # Base Test Execution
