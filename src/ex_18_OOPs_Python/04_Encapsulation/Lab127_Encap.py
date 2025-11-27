class Car:

    # Good Practice to define the instance variables
    name = None
    make = None
    model = None

    # Parameterized Constructor
    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model

    # Method
    def start_engine(self):
        print("Starting car with name: "+self.name)
        print("Starting car with make: "+self.make)
        print("Starting car with model: "+self.model)

lambo = Car("lambo", "V6", "2023")
lambo.start_engine()

mg_hector = Car("Hector", "1.5+ Turbo", "2023")
mg_hector.start_engine()



