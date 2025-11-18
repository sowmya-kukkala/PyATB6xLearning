# Defining the decorator
def add_security(func):         # defining annotation which takes function as input
    def wrapper():
        # define the actions before calling the function
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcash, gloves, knee guards, License")
        # func() defines to call the drive_ola_Scooters function
        func()
        # define the actions after calling the function
        print("3. After the function is called")
        print("4. Secure Driving, Leave all the items")
    return wrapper

@add_security
def drive_ola_scooters():
    print("I am driving ola scooter")

# We can re-use the decorator to any other function by adding the decorator as annotation

@add_security
def drive_zypp_scooters():
    print("I am driving zypp scooter")

drive_ola_scooters()
drive_zypp_scooters()

