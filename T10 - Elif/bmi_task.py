weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = weight / (height * height)

if BMI >= 30:
    print("obese")
elif BMI >= 25:
    print("overweight")
elif BMI >= 18.5:
    print("normal")
elif BMI < 18.5:
    print("underweight")