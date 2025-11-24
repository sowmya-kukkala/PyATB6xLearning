class Person:
    # Note: if we define the attributes under constructor/method directly using self,
    # python automatically creates attributes where values set to None (in backend)

    def __init__(self):
        print("Let's take the user input, Please share the name, age, phone, occupation")
        self.name = input("Enter your name: \n")
        self.age = input("Enter your age: \n")
        self.phone = input("Enter your phone: \n")
        self.occupation = input("Enter your occupation: \n")

    def display_person_details(self):
        # self.role = input("Enter your role: \n")
        print("Name is: ",self.name, ", Age is: ",self.age, ", Phone is: ",self.phone, ", Occupation is: ",
              self.occupation)


# Person().display_person_details()

amit = Person()
amit.display_person_details()