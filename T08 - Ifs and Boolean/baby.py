birthyear = int(input("Enter your birth year: "))

current_year = 2022 # can be replaced with import datetime year

age = current_year - birthyear
if age >= 18:
    print("Congrats you are old enough")
else:
    print("Come back later")
