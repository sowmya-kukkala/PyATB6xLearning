class InvalidAgeException(Exception):
    pass

def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide by zero")


def can_you_drink(age):
    if age < 18:
        raise Exception("Invalid age to drink")

# print(can_you_drink(17))
print(check_zero_div(0))
