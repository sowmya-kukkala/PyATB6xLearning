class Dog:
    # Attributes - Instance Variables | Data Variables
    name = None
    breed = None
    height = None
    weight = None
    race = None

    def __init__(self, namegiven, breedgiven):
        print("Parameterized Constructor")
        self.name = namegiven
        # print(self.name)
        self.breed = breedgiven
        # print(self.breed)

    # Behaviour
    def bark(self):
        print("Barking")

    def sleep(self):
        print("Who is sleeping ? -> " + self.name)

    def talk(self):
        pass

chow = Dog("Chow", "Mastiff")
rancho = Dog("rancho", "desi")

chow.sleep()
rancho.sleep()