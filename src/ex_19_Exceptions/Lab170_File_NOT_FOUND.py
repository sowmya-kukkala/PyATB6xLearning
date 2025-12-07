try:
    data = open("test.json").read()
except FileNotFoundError as fnf:
    print(fnf)

# Output
# [Errno 2] No such file or directory: 'test.json'