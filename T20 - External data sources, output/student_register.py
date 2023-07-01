with open('./reg_form.txt', 'w+') as f:

    # Input number of students registered
    num_of_students = int(input("Enter number of registered students: "))
    
    # Write field to file
    f.write(f"Registration Form ID\n\n")
    
    # Loop for number of students
    for i in range(num_of_students):

        # Input ID
        id_number = input("Enter student's ID number: ")
    
        # Write ID to file
        f.write(f"{id_number}    {'.'*20} \n\n")

f.close