# If Base Classes have same method name, Python always calls based on the order in which Base Classes called.
# Also, known as MRO (Method Resolution Order)

class Father1:
    def money(self):
        print("F1 Money")

class Father2:
    def money(self):
        print("F2 Money")

# Scenario 1- Calls Father1 method
# class Child(Father1, Father2):
#     def give_money(self):
#         print("Son")
#         self.money()

# Scenario 2 - Calls
class Child(Father2, Father1):
    def give_money(self):
        print("Son")
        self.money()

# Scenario 1 - related
# c = Child()
# c.give_money()
# Son
# F1 Money

# Scenario 2- related
c = Child()
c.give_money()
# Son
# F2 Money

