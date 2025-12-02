class MathClass:
    def add(self,a,b):
        return a+b

    # Scenario 1:
    # def add(self,a,b,c):
    #     return a+b+c

    # Scenario 2:
    def add(self,a,b,c=10):
        return a+b+c



# Note: By default, Python doesn't provide which parameters represents what datatype

# Here, in the above case, since the methods are same, it always calls the latest method.
# i.e., that has three methods

obj_ref = MathClass()

# Scenario 1:
# print(obj_ref.add(1,2)) # Invalid
# print(obj_ref.add(3.14,4.14,3)) # 10.28

# Scenario - 2:
print(obj_ref.add(1,2)) # 13

# In both scenarios, always the latest method will be called given we provide default value or not