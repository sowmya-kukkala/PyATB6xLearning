class Calc:
    a = None
    b = None

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Note: We can have multiple parameterized constructors having different attributes/variables w.r.t Arguments
    # def __init__(self,a,b,c):
    #     self.a = a
    #     self.b = b
    #     self.c = c

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

object_ref = Calc(20,10)
output_sum = object_ref.sum()
output_sub = object_ref.sub()
output_mul = object_ref.mul()
output_div = object_ref.div()

print(output_sum, output_sub, output_mul, output_div)
