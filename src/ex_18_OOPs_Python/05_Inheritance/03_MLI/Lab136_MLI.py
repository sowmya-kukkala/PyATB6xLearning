class TestSuite:
    def info(self):
        print("This is GF - Step 1")

class BaseTest(TestSuite):
    def setup(self):
        print("This is Base Test - F - Step 2")

class UITest(BaseTest):
    def run(self):
        self.info()
        self.setup()
        print("Running Test Case")

test = UITest()
test.run()

# This is GF - Step 1
# This is Base Test - F - Step 2
# Running Test Case