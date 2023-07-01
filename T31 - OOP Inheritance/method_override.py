class Adult:
    # Assign constructors to 'Adult' class
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour
    
    # Method 'can_drive'
    def can_drive(self):
        print(f"{self.name} is old enough to drive")

class Child(Adult):

    # Inherit constructors from Adult class
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)
    
    # Overwrite method 'can_drive'
    def can_drive(self):
        print(f"{self.name} is too young to drive")

# Prompt user to enter person's details
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
eye_colour = input("Enter person's eye colour: ")
hair_colour = input("Enter person's hair colour: ")

# Determine if person belongs in 'Adult' or 'Child' class
if age >= 18:
    person = Adult(name, age, eye_colour, hair_colour)
    person.can_drive()
else:
    person = Child(name, age, eye_colour, hair_colour)
    person.can_drive()
