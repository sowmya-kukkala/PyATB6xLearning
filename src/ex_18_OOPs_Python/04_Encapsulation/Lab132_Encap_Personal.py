class Home:
    def __init__(self):
        self.public_var = "PepaGrandPapa"
        self._protected_var = "PepaBro"
        self.__private_var = "PepaPig"

    # Public method can access private variables and methods
    def pepagrandma(self):
        print(self.__private_var)
        self.__pepamama()

    def __pepamama(self):
        print("Private Pepa Mama")

object_ref = Home()
# object_ref.__pepamama() # Invalid
object_ref.pepagrandma()
# PepaPig
# Private Pepa Mama
# print(object_ref._protected_var) # PepaBro # Note: Technically accessible but not recommended
