# Hybrid Inheritance is a combination of Hierarchical and Multiple Inheritances (Indirectly, Multi-level also applied)

# Hierarchical Inheritance
class Base:
    def base_method(self):
        print("Base Method")

class A(Base):
    def a_method(self):
        print("A Method")

class B(Base):
    def b_method(self):
        print("B Method")

# Multiple Inheritance
class C(A,B):
    def c_method(self):
         print("C Method")

obj = C()
obj.base_method()
obj.a_method()
obj.b_method()
obj.c_method()

# Base Method
# A Method
# B Method
# C Method