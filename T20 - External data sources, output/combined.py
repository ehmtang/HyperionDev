# Write to numbers1
with open('./numbers1.txt', 'w+') as f1:
    
    # Create first array and sort
    arr1 = [4, 2, 1, 9, 11]
    arr1.sort()

    # Write array to numbers1
    f1.write(f"{arr1}")

f1.close

# Write to numbers2
with open('./numbers2.txt', 'w+') as f2:
    
    # Create second array and sort
    arr2 = [13, 3, 5, 7, 11]
    arr2.sort()

    # Write array to numbers2
    f2.write(f"{arr2}")

f2.close

# Write to all_numbers
with open('./all_numbers.txt', 'w+') as f3:
    
    # Create third array from arr1 and arr2 and sort
    arr3 = arr1 + arr2
    arr3.sort()

    # Write array to all_numbers
    f3.write(f"{arr3}")

f3.close