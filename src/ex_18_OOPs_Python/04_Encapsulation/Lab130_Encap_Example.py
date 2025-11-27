# Encapsulation -
# Hide the data members (class variables/instance variables)
# by using only methods

class Car:
    def __init__(self):
        self.password = "pramod"        # public variable that can be accessible outside
        self.__password__ = "pass123"   # private(name starts with __) variable that can't be accessible outside

    # Private variables can only be accessed through method - To use the value or to modify the value
    def details(self):
        # self.__password__ = "345"
        print(self.__password__)


car_object_ref = Car()
print(car_object_ref.password) # pramod
# print(car_object_ref.__password) # Invalid
car_object_ref.details() # pass123
