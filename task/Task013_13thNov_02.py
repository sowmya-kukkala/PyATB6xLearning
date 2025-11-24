# You need to create a calculator function, but the calculator function has to take the value
# from the parameterized constructor. So while creating the object,
# you will pass the parameters and that will basically return the sum of the two numbers,
# multiplication of two numbers.

class Calculator:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def sum(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b

object_ref = Calculator(20,2)
print(object_ref.sum())
print(object_ref.mul())