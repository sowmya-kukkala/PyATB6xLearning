# Q - Create a function which will take the 3 values from the user, which are length of the triangle.
# side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def triangle_classifier(side1, side2, side3):
    if side1 > 0 and side2 > 0 and side3 > 0:
            if side1+side2 > side3 and side1+side3 > side2 and side2+side3 > side1:
                if side1 == side2 == side3:
                    return "Equilateral Triangle"
                elif side1 == side2 or side2 == side3 or side3 == side1:
                    return "Isosceless Triangle"
                else:
                    return "Scalene Triangle"
            else:
                print("Not a Triangle")
    else:
        print("Not a valid side length")

result = triangle_classifier(50, 50, 50)
print(f"The Triangle is classified as: {result}")

