
list_of_names = []

# Infinite loop to ask for a name
while True:

    my_string = input("Enter a name: ")
    
    # Break if input is equal to John (case insensitive)
    if my_string.lower() == "John".lower():
        break

    # Append incorrect names to list
    list_of_names.append(my_string)

print("Incorrect names: " f"{list_of_names}")
