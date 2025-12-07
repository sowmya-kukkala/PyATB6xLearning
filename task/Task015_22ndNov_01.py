# Q - Create a framework base counter that counts test execution instances:

class Base_Counter:
    count = 0

    def __init__(self):
        Base_Counter.count += 1

test_execution1 = Base_Counter()
test_execution2 = Base_Counter()
test_execution3 = Base_Counter()

print("The total count of test execution instances: ",Base_Counter.count)
