# Write a program to calculate even and odd
# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

user_input = int(input("Enter a number: "))
find_even_odd_l = lambda num: "Even" if num%2 == 0 else "Odd"
print(find_even_odd_l(user_input))