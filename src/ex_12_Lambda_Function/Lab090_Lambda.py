def triple_number(num):
    return num * num * num

result = triple_number(3)
print(result) # 27

# Lambda - Can be used if it has only single line statement to process.
# But not applied if it has more than one statement.
# However, using ternary operator we can add one if-else statement
result_l_func = lambda num: num * num * num
print(result_l_func(3)) # 27