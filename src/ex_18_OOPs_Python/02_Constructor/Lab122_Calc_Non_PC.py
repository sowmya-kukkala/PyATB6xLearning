class Calc:
    a = None
    b = None

    # Scenario - 1: Can we create more than one default constructor - Yes. However, it takes the latest one
    # def __init__(self):
    #     print("DC")
    #
    # def __init__(self):
    #     print("DC2")

    # Scenario - 2: Having one default constructor and parameterized constructor
    # Where the parameterized constructor will be called in this scenario but not the default constructor
    # def __init__(self):
    #     print("DC")
    #
    # def __init__(self,a,b):
    #     print("PC")

    # Scenario -3:
    def __init__(self):
        print("DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

# Calc() # DC2 --> Scenario 1 output

# Calc('hello', 'hi') # PC --> Scenario 2 - output

# Scenario 3:
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

object_ref = Calc()
output_sum = object_ref.sum(a, b)
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_div = object_ref.div(a, b)
print(output_sum, output_sub, output_mul, output_div)