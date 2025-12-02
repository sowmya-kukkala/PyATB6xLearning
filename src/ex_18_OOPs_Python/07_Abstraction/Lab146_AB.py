from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Amit(Father):
    def loan(self):
        print("Giving the 50K Loan")

amit = Amit("AMIT SHARMA")
amit.loan() # Giving the 50K Loan