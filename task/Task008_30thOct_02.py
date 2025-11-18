# Q - Create a function which will take the 3 values from the user, which are length of the triangle.
# side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

def sides_of_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "Equilateral Triange"
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Isosceless Triange"
    else:
        return "Scalene Triangle"


result = sides_of_triangle(int(input("Enter side1 value: ")),
                           int(input("Enter side2 value: ")),
                           int(input("Enter side3 value: ")))
print(result)

