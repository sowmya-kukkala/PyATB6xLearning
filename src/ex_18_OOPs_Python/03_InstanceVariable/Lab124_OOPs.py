a = 10      # Global variable - that's available everywhere

class Person:
    b = 11  # Instance variable - accessible within the class

    def print_info(self):
        c = 20  # local variable - accessible within the method
        print(c)
        print(self.b)
        print(c)

object_ref = Person()
# print(b) # Invalid to call
# print(c) # Invalid to call
print(a)  # 10