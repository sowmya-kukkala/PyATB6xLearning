# Given a Number, a number you need to calculate the factorial of that number
# n = 5
# Fact = 5×4×3*2*1 = 120
# Fact = 0 → 1

num = int(input("Enter a number to find the factorial:\t").strip())
#num = 5
fact = 1
if num<0:
    print("The factorial of",num," NOT CONSIDERED FOR CALCULATION")
elif num == 0:
    print("The factorial of",num," is: ", fact)
else:
    for i in range(fact,num+1):     # 1 2 3 4 5
        fact = fact*i                               # 1 # 2 # 6 # 24 # 120
    print("The factorial of ", num , " is: ", fact)




