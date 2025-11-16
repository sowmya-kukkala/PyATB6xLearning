public_toilet = "PB"

# Scenario - 1

def home():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)

home()


# Scenario - 2
def stranger():
    print(public_toilet)
    # print(private_toilet)   #  Invalid - Scope of the private_toilet variable is within home()

stranger()

