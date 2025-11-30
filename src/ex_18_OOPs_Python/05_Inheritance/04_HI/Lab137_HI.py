# In Hybrid Inheritance, C can have access only to B, However, through B only, C can access A
class BaseTest:
    def setup(self):
        print("Setup from Base Test")

class LoginTest(BaseTest):
    def run(self):
        print("Running Login Test")

class SignupTest(BaseTest):
    def run(self):
        print("Running Signup Test")

test = LoginTest()
test.setup()
test.run()

test = SignupTest()
test.setup()
test.run()


# Setup from Base Test
# Running Login Test
# Setup from Base Test
# Running Signup Test