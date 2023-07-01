num = float(input("Enter a number less than or equal to 100: "))

# Loop until conditions are met
while num > 100:
    num = float(input("Enter a number less than or equal to 100: "))

# number is even
if (num % 2) == 0:
    print(num*2)

# number is odd
else:
    print(num*3)
