set1 = set(["TheTestingAcademy", "for", "TheTestingAcademy."])
print(set1) # {'TheTestingAcademy.', 'for', 'TheTestingAcademy'}
print(len(set1)) # 3

# Read the individual elements
for item in set1:
    print(item)

# TheTestingAcademy.
# TheTestingAcademy
# for

set1.add("SDET")
set1.add("SDET")

print(set1)  # {'TheTestingAcademy', 'SDET', 'TheTestingAcademy.', 'for'}