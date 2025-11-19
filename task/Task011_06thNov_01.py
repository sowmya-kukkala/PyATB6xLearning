# Right Angled Triangle

# Method 1:

# for i in range(1, 6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print()

# Method 2:
for i in range(5):
    for j in range(5):
        if(i>=j):
            print("*", end=" ")
        else:
            print(end=" ")
    print()