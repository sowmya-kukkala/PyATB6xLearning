import os

# file_path = os.path.join(r"C:\Users\Sowmya\PycharmProjects\PyATB6xLearning\src\ex_22_Collections","promo.txt")
file_path = os.path.join(os.getcwd(), "promo.txt")
# print(file_path)

file = open(file_path, 'r')
print(file.read()) # Hello, How are you ?

file.close() # Ensure to close the opened file


