a = int(input("Enter num 1: ")) # 10
b = int(input("Enter num 2: ")) # 10 # 0
try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error because of the zero division where it has to be b!=0 ")
