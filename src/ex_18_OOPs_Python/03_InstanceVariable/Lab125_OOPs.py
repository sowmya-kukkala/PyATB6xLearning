count = 0

def increment():
    global count  # if we use global, then we are saying that earlier count variable will be overridden by this variable
    # given global can be used within the method or class, to make the variable available globally to access everywhere
    count += 1

increment()
increment()
increment()
print(count) # 3