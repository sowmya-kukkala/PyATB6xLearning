import csv

with open('TD.csv') as csvfile:             # By default set to read mode for .csv file(s)
    file_reader = csv.reader(csvfile)
    for col in file_reader:
        print(col[0], col[1], sep='|')

# username|password
# admin|password123
# admin123|pass123