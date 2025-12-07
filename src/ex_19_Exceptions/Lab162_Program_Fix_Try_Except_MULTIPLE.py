a = int(input("Enter num 1: ")) # 10
b = int(input("Enter num 2: ")) # 10 # 0
try:
    c = a / b
    print(c)
except (TypeError, NameError, ValueError, ZeroDivisionError):
    print("Error might occurred due to Type, Name, Value or Zero Div!")

# Providing String instead of int can also be tested

