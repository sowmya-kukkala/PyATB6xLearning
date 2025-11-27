class TestExample:
    def __init__(self):
        self.driver = "Chrome"
        self._config = "STAGE" # Protected variables can be access within class and directory but not in other directory
        self.__api__key = "ABC12345"

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    # Private method is used to hide any given details
    def __private_method1(self):
        print("Private method1")

    def __private_method2(self):
        print("Private method2")

    # Public methods can access the private methods and variables
    def work(self):
        self.__private_method1()
        self.__private_method2()

object_reference = TestExample()
object_reference.show()
# Driver: Chrome
# Config: STAGE
# API Key: ABC12345

# Access Levels
print(object_reference.driver) # Chrome -> Valid
print(object_reference._config) # STAGE -> Technically allowed but not recommended
# print(object_reference.__api__key) # AttributeError -> Invalid
# print(object_reference._TestExample__api__key) # ABC12345 -> Accessible via class name (as protected) to access private variable

object_reference.work()
# Private method1
# Private method2