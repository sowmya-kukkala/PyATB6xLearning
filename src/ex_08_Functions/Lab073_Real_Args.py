# Pizza Lovers
# Toppings - Corn , Paneer, Olive, Cheese, Pineapple, Jalapelano, Capsicum, Tomato

def make_pizza(*toppings):
    print(toppings)

user1 = make_pizza("Cheese", "Corn")
user2 = make_pizza("Cheese", "Corn", "Panner", "Capsicum")
user3 = make_pizza("Tomato","Jalapelano")

# Returns result as below -

# ('Cheese', 'Corn')
# ('Cheese', 'Corn', 'Panner', 'Capsicum')
# ('Tomato', 'Jalapelano')
