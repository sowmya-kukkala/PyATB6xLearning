for i in range(5):
    # Scenario 1: Using pass - does nothing
    # if i == 3:
    #     pass
    # print(i)     # Prints 0 1 2 3 4

    # Scenario 2: Using Continue - skips
    if i == 3:
        continue
    print(i)  # Prints 0 1 2 4