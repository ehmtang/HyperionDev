num = int(input("Enter a positive integer: "))

# Condition number greater than 10 to loop print that many times
if num > 10:
    for i in range(num):
        print(num)

# Condition less or equal to print prompt
elif num <=10:
    print("Sorry, too small")