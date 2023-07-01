# List of numbers from 1 to 1000
one_to_thousand = list(range(1,1001))

# Print number in list that is even
for idx, num in enumerate(one_to_thousand):
    if (num % 2) == 0:
        print(num)