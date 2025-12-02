# Abstraction - Hide the details and show what is required

# Car -> with Key _ __ private, tyres --> Public
# Car -> multiple --> Engine, Gearbox
# Car -> driver --> Engine, Gearbox

# Note: If we set a class as Abstract then 2 points to follow
# 1.) inherit ABC class
# 2.) given method set to abstract then need not provide the details in the method for the given class.
# Since the implementation will be provided in the inherited Class

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog("PP")
dog.sound() # Bark

