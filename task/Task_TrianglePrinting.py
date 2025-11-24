# *
# * *
# * * *
# n = 3

rows  = int(input("Enter the rows to construct Right Traingle: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end = "")
    print()

# for i in range(1,rows+1):
#     print("*" * i)

