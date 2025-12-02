class Utility:
    @staticmethod
    def greet_course_name(name):
        print("Hi,", name)

    def greet_personal(self, name):
        self.name = name
        print("Hello,", self.name)


t = Utility()
t.greet_course_name("PyATB") # Hi, PyATB
t.greet_personal("Smith") # Hello, Smith