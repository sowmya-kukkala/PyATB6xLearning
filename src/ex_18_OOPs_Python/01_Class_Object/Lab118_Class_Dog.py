class Dog:
    # Atrributes
    name = None
    breed = None
    height = None
    weight = None

    # Behaviour
    # use self to access the attributes of the class
    def bark(self):
        print("Barking")
        print(self.name)

    def talk(self):
        print("Talking")

chow = Dog()
rancho = Dog()
# Dog() -> Object
# chow -> Object Reference


