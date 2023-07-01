
list_of_pupils = []

# Infinite loop
while True:
    # Input pupils' names
    names_of_pupils = input("Enter names of pupils: ")
    
    # Condition to break
    end_loop = "stop"
    if names_of_pupils.lower() == end_loop.lower():
        break

    # Append names to list
    list_of_pupils.append(names_of_pupils)

print(f"List of pupil's names: {list_of_pupils}")
print(f"Number of pupils in class: {len(list_of_pupils)}")