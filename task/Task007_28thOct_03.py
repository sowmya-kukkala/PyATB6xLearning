# Skip numbers divisible by 3, from (0,100)

for num in range(0,101):
    if num % 3 == 0:
        continue
    print(num)