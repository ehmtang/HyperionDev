num = int(input("Enter an integer: "))

if (num % 2) == 0 and (num % 5) == 0:
    print(f"{num} divisible by 2 and 5")

elif (num % 2) == 0 or (num % 5) == 0:
    print(f"{num} divisible by 2 or 5")

else:
    print(f"{num} not divisible by 2 or 5")
