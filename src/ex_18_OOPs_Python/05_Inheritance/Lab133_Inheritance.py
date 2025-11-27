# Single Inheritance

# A Sub-class/Child inherits from one Base/Parent

class BaseTest:
    driver = "Chrome"
    __driver2 = "FF" # private variables from Base Class can't be accessed by sub-class directly.

    # But the Base class methods can access the private variables from which we can call the method into Sub-class
    def setup(self):
        print("Base Setup with Browser and Environment in", self.__driver2)

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the Test Cases in", self.driver)
        # print("Running the Test Cases in", self.__driver2) # AttributeError

obj_ref = LoginTest()
obj_ref.run()
# Base Setup with Browser and Environment in FF
# Running the Test Cases in Chrome