class Person:
    def say_name(self, name):
        print("Hi,", name)

    # Scenario 1: When no default value is provided
    # def say_name(self, fname, lname):
    #     print("Hi,", fname, lname)

    # Scenario 2: When default value is provided
    def say_name(self, fname, lname="Smith"):
        print("Hi,", fname, lname)



# Note: Python considers that a particular method to be called based on the maximum no. of parameters available

obj_ref = Person()
# Scenario 1:
# obj_ref.say_name("John", "Smith") # Hi, John Smith
# obj_ref.say_name("John") # TypeError: Person.say_name() missing 1 required positional argument: 'lname'

# Scenario 2:
obj_ref.say_name("John") # Hi, John Smith