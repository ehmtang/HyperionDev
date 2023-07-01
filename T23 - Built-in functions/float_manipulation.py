import math
import statistics

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter forth number: "))
num5 = float(input("Enter fifth number: "))
num6 = float(input("Enter sixth number: "))
num7 = float(input("Enter seventh number: "))
num8 = float(input("Enter eighth number: "))
num9 = float(input("Enter ninth number: "))
num10 = float(input("Enter tenth number: "))

list_of_num = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

# The sum of the list of numbers
total = math.fsum(list_of_num)
print(total)

# max value and its index
max_num = max(list_of_num)
max_num_index = list_of_num.index(max_num)
print(f"{max_num_index} : {max_num}")

# min value and its index
min_num = min(list_of_num)
min_num_index = list_of_num.index(min_num)
print(f"{min_num_index} : {min_num}")

# average and round off to 2 decimal places
# It's easier to import statistics module to compute the arithmetic average
avg = statistics.mean(list_of_num)
print(math.ceil(avg*100)/100)

# median
# It's easier to import statistics module to compute the median
median = statistics.median(list_of_num)
print(median)