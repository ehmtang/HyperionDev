# Open DOB file
with open('./DOB.txt', 'r+') as f:

    # Create empty lists for names and birthdates
    list_of_names = []
    list_of_birthdates =[]

    # Loop lines in DOB file.Split name and birthdate by second whitespace into two lists
    for line in f:

        name = " ".join(line.split(" ")[:2])   
        list_of_names.append(name)
        birthdate = " ".join(line.split(" ")[2:])
        list_of_birthdates.append(birthdate)

    print("Name")

    # Print each name contained in list
    for name in list_of_names:
        print(name)

    print()

    print("Birthdate")

    # Remove new line from list
    list = []
    for birthdate in list_of_birthdates: # alternative line of code = [x.strip() for x in list_of_birthdates]
        print(birthdate.strip())
        list.append(birthdate)

# Close file
f.close()


"""
References

https://stackoverflow.com/questions/42126894/python-split-strings-at-a-specific-whitespace

used to split string by index, in this case by second whitespace

https://www.pythonpool.com/python-remove-newline-from-list/

used to remove new line from list

"""