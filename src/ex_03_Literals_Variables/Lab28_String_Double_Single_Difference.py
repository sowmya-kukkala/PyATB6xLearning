c = 'C'
c1 = "C"
# print(c)
# print(c1)

# dir = 'C:\sowmya\n.txt' # Invalid - since it considers escape sequence
dir = r"C:\sowmya\n.txt"
print(dir) # C:\sowmya\n.txt

# Note: r indicates raw - it will print as it is (Ignores the escape sequence)

file_path = r"/src/ex_03_Literals_Variables/Lab28_String_Double_Single_Difference.py"
print(file_path)