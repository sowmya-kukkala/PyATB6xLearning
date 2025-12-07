# Available from Python 3.11

mul_exceptions = ExceptionGroup("Multiple Exceptions",
                                [ValueError("Invalid Value"),
                                 TypeError("Type Error"),
                                 ZeroDivisionError("Can't divide by zero")])

def check_div(a):
    if a == 0:
        raise mul_exceptions

print(check_div(0))
