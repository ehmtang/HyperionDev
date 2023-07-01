# Infinite loop

list_of_numbers =[]

while True:

    # user input integer
    num = int(input("Enter a number: "))

    # Condition to break
    if num == -1:
        break

    # Append number to list
    list_of_numbers.append(num)

average_of_numbers = sum(list_of_numbers) / len(list_of_numbers)
print(f"The average of the numbers is: {average_of_numbers}")