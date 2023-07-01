shape_of_building = input("Enter shape of building: ")

if shape_of_building == "square":
    length = float(input("Enter length dimension: "))
    area = length**2
    print(area)

elif shape_of_building == "rectangular":
    width = float(input("Enter width dimension: "))
    length = float(input("Enter length dimension: "))
    area = width * length
    print(area)

elif shape_of_building == "round":
    radius = float(input("Enter radius dimension: "))
    import math
    area = math.pi * radius**2
    print(area)