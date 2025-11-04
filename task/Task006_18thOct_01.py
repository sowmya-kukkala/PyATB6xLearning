# Given a Number, a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1

n = int(input("Enter a number to find the factorial:\t").strip())
fact = 1
if n<0:
    print("Invalid input")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(fact,n+1):
        fact = fact*i
print("The factorial of ", n , " is: ", fact)




