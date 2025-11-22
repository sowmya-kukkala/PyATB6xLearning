response_times_ms = [1200, 1500, 1800]

# Method 1:
# def milli_seconds(x):
#     return x/1000

# response_times_in_seconds = list(map(milli_seconds, response_times_ms))
# print(response_times_in_seconds) # [1.2, 1.5, 1.8]

#Method 2:
# Convert above function to lambda
# milli_seconds = lambda x: x / 1000

# response_times_in_seconds = list(map(milli_seconds, response_times_ms))

response_times_in_seconds = list(map(lambda x: x / 1000, response_times_ms))
print(response_times_in_seconds) # [1.2, 1.5, 1.8]


