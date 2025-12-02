class MathOperation:
    def div(self,a,b):
        return a/b

    @staticmethod
    def add(a,b):
        return a+b

t = MathOperation()
print(t.div(10,10)) # 1.0
print(MathOperation().div(10,10))  # 1.0
print(MathOperation.add(10,10)) # 20

# Note: For Non-static methods you have to create the object instance/reference.
# However, for static methods we can call them directly with the class name