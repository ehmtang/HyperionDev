side1 = float(input("Enter length of first triangle side: "))
side2 = float(input("Enter length of second triangle side: "))
side3 = float(input("Enter length of third triangle side: "))

# Formula to calculate the area of a triangle
s = (side1 + side2 + side3)/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print(area)