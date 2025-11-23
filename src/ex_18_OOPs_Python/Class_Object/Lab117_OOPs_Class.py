class Person:
    # pass   # defined to represent it doesn't have anything to execute
    # Attributes
    name = None
    id = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None

    # Behaviour - Also, known as Method - as it is defined within the class
    # self - Always will be first argument for every method we define
    def talk(self):
        print("I can talk")

    # Argument with No return
    def sleep(self , name):
        print("I am a Method!!")
        print("Sleep", name)

    # Argument with return
    def sleep2(self,name):
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    # No Argument with return
    def method_walk_return(self):
        return "I am walking"

# Since this is defined outside the class, we say it as function
def function_outside():
    print("I am outside")

# Create an Object of the class
# ObjectRef = ClassName() -> Object

geeta = Person() # Here geeta is reference variable, Person() - refers to object created
print(geeta.name) # Accessing the attributes of the class
print(geeta.walk()) # Accessing the methods of the class
print(geeta.sleep("Hello")) # Accessing the methods of the class

amit = Person()
navita = Person()

