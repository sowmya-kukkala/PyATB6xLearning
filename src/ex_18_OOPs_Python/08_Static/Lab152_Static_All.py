# Static Methods
# A Static method is a method that belong to a class rather than an instance of the class

class Demo:
    @staticmethod
    def sum(a,b):
        return a+b

# t = Demo() # Static methods can be accessed directly
print(Demo.sum(1,2)) # 3