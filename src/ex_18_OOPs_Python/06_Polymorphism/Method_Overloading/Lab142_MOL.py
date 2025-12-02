class MathClass:
    def add(self,a,b):
        return a+b

    def add(self,a,b):
        return a+b

# Note: By default, Python doesn't provide which parameters represents what datatype

# Hence, in the defined two methods we don't know which is getting called and by default calls the latest method only

obj_ref = MathClass()
print(obj_ref.add(1,2))
print(obj_ref.add(3.14,4.14))