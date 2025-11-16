# User-Defined

# 1. No Return Type and No Parameter / Argument - NRNP
# They can't return -> non-return
def greet():
    print("Hello")

greet()

# 2. No Return Type and with Argument/ Param
def greet_by_name(name):
    print("Hi,",name)

greet_by_name("Sowmya")

# 3. No Return Type and with Default Argument (# Positional Arguments)

# Scenario 1:
def say_hello_default_arg(name="sdet"):
    print("Hello", name.upper())

say_hello_default_arg()
say_hello_default_arg("Sai")

# Scenario 2:
def multiple_args(name1="A", name2="B"):
    print("Mul ->", name1, name2)

multiple_args()     # Mul -> A B
multiple_args(name1="Sample", name2="Test") #  Mul -> Sample Test
multiple_args(name1="Sample1") # Mul -> Sample1 B
multiple_args(name2="Test2") # Mul -> A Test2

# 4. Arguments + Return Type

def sum_of_two(a, b):
    return a+b

result = sum_of_two(20, 2)
print(result) # 22

def sum_of_two_numbers_with_default(num1=100, num2=200):
    print("I will be sum of two numbers!")
    return num1+num2

result = sum_of_two_numbers_with_default()
print(result)
result = sum_of_two_numbers_with_default(num1=34, num2=56)
print(result)

# build-in functions

import math
result = max(3,5)
print(result) # 5

