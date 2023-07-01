full_name = input("Enter your full name: ")

# input is empty
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")

# input is less than 4 characters
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that ou have entered your name and surname")

# input is more than 25 characters
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# input satisfy conditions
else:
    print("Thank you for entering your name")