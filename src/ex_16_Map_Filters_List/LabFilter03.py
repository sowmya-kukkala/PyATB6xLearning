names = ["QA", "", "Automation", "", "Tester"]

# Method 1:
# print_names = list(filter(lambda x: x!="", names))
# print(print_names)  # ['QA', 'Automation', 'Tester']

# Method 2:
# def non_empty(x):
#     if x != "":
#         return True
#     return None

# non_empty = list(filter(non_empty, names))
# print(non_empty)  # ['QA', 'Automation', 'Tester']

# Method 3:
# non_empty = list(filter(None, names))
# print(non_empty) # ['QA', 'Automation', 'Tester']

