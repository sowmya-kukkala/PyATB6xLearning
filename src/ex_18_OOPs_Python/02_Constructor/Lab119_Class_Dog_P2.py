print("Outside the class")

class MobilePhone:
    model = None

    # Constructor -> Used to initialize the attribute value
    def __init__(self):
        print("Default constructor")

    def talk(self):
        print("Hi, Talking")

iphone = MobilePhone()
iphone.talk()
print("Outside the class2")