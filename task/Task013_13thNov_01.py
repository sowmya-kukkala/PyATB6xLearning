# Create a Person class where we will have five attributes and five behaviors.
# Make sure that each type of function is used, and I want you to also create the print function,
# which will print all the instance variable values.

class Person:
    name = None
    age = None
    gender = None
    role = None
    team = None

    def walk(self):
        print("walk")

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def study(self):
        print(self.name," can study")

    def work(self):
        print("Being in ", self.role, "will work")

    def display_details(self):
        print("Please provide the following inputs: ")
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.gender = input("Enter your gender: ")
        self.role = input("Enter your role: ")
        self.team = input("Enter your team: ")
        print("The details as follows: ", "Name is: ", self.name,
              ", Age is: ", self.age, ", Gender is: ", self.gender,
              ", Role is: ", self.role, ", Team is: ", self.team)

object_ref = Person()
object_ref.display_details()
object_ref.study()
object_ref.work()
object_ref.eat()
object_ref.walk()
object_ref.sleep()


