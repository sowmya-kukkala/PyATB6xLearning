try:
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    c = a / b
except TypeError:
    print("Type Error")
except ZeroDivisionError:
    print("Zero Division Error")
else:   # Runs only if try block succeeds
    print(c)
finally:
    print("I will always be executed!")

# Note: If 'try' block succeeded then execute the 'else' block.Else, execute the relevant 'except' block. But by
# default finally block will be executed



