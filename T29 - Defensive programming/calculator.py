import re

def read_calc():
    
    # Read file and print equations
    # if file not found raise exception 
    while True:
        filename = input("Enter filename to be read: ")
        try:
            with open(f'./{filename}.txt', 'r') as input_f:
                print(input_f.read())
                break
        except FileNotFoundError as error:
            print("The file that you are trying to open does not exist.")
            print(error)

def calculator():
    
    # Ask user for first number
    # Raise exception if number is invalid ie not a float
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except Exception:
            print("First number is invalid number")
    
    # Ask user for operator
    # Raise exception if operator is invalid from list "+ - x /"
    operator = input("Enter an operator: ")
    if operator not in ('+', '-', 'x', '/'):
        raise Exception("Operator is invalid.")
    
    # Ask user for first number
    # Raise exception if number is invalid ie not a float
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except Exception:
            print("Second number is invalid number")

    # Calculate answer dependent of inputs
    if operator == '+':
        ans = num1 + num2

    elif operator == '-':
        ans = num1 - num2

    elif operator == 'x':
        ans = num1 * num2

    elif operator == '/':
        ans = num1 / num2

    # Prompt user to enter a filename for output
    # Raise exception if special character used
    filename = input("Enter a filename for the output file: ")
    pattern = pattern = r'[^a-zA-Z0-9_\s]'
    if re.search(pattern, filename):
        raise Exception("Filename contains special character.")
    
    # Append to file if it exists
    # Otherwise write new file
    with open(f'./{filename}.txt', 'a') as output_f:
        output_f.write(f"{num1} {operator} {num2} = {ans}\n")
    
    return

# Create option for user to select calculator or read_calc functions
menu = input("Enter option 'c' to open calculator or 'r' to read calculator: ").lower()

if menu == 'c':
    calculator()
elif menu == 'r':
    read_calc()
else:
    print("Option not valid.")

