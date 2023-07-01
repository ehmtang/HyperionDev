num = int(input("Enter an integer: "))
n = 1

# Loop while 'n' is less than input
while n <= num:
    
    # Increment
    n = n + 1

    # Print only even numbers
    if (n % 2) == 0:
        print(n)
    