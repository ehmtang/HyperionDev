i = 21
while i > 0:
    i = i - 1
    print(i)

print()

for j in range(1,21):
    if (j % 2) == 0:
        print(j)

print()

for k in range(6):
    print("*"*k)

print()

# Reference from https://www.pd4cs.org/example-12-find-the-greatest-common-divisor-gcd-of-two-integers/

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))


while num2 != 0:
    gcd = num2
    num2 = num1 % num2
    num1 = gcd
print(gcd)

# Loop from 1 to num2+1
for i in range(1, num2+1):
    
    # Check if both num1 and num2 are divisible by i
    if num1 % i == 0 and num2 % i == 0:
        
        # Let gcd = i, loop ends with largest possible value of i
        gcd = i
print(gcd)