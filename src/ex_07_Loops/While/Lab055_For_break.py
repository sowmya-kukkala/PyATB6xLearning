for i in range(0,10):
    # Scenario 1: First prints then checks condition
    print(i)        # prints 0 to 5
    if i == 5:
        break

    # Scenario 2: First checks condition then prints
    # if i == 5:
    #     break
    # print(i)   # prints 0 to 4