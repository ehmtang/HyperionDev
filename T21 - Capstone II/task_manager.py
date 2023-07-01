#=====importing libraries===========
from datetime import datetime

#====Login Section====

# Open user.txt and store user login information as a dictionary
with open('./user.txt', 'r') as user_file:

    #Create empty dict to store user login information
    login_dict = {}

    # For each new line in user file, split line into elements
    # Assigning first element 'user' as key
    # and second element 'password' as value 
    for line in user_file:
        list = line.split(', ')
        login_dict[list[0]] = ''.join(list[1].split())

# Infinite loop prompt user for username
# If username exists, break loop
while True:

    user_input = input("Enter username: ")

    if user_input not in login_dict.keys():
        print("Username not found. Try again.\n")
    
    else:
        break

# Infinite loop prompt user for password for user_input
# If password is correct for user, break loop
while True:

    password_input = input("Enter password: ")

    if password_input != login_dict[user_input]:
        print("Password is incorrect. Try again.\n")
    
    else:
        break

print(f"Hi {user_input}, you have successfully logged in.")

with open('./tasks.txt', 'r') as tasks_file:

    # Create empty dict following tasks_file format
    tasks_dict ={
        'user':[],
        'task':[],
        'task_descr':[],
        'issue_date':[],
        'due_date':[],
        'completion':[]
        }

    # For each line in tasks append the following keys:
    #   - user, 
    #   - task, 
    #   - task description, 
    #   - issue date, 
    #   - due date, 
    #   - completion 
    # into the dictionary. Note, values stored as a list
    for line in tasks_file:
        list = line.split(', ')
        
        user = ' '.join(list[0].split())
        tasks_dict['user'].append(user)
        
        task = ' '.join(list[1].split())
        tasks_dict['task'].append(task)

        task_descr = ' '.join(list[2].split())
        tasks_dict['task_descr'].append(task_descr)

        # Note: dates convert from string inputs to conventional date format DD MMM YYYY
        issue_date = ' '.join(list[3].split())
        issue_date = datetime.strptime(issue_date, '%d %b %Y')
        tasks_dict['issue_date'].append(issue_date)

        due_date = ' '.join(list[4].split())        
        due_date = datetime.strptime(due_date, '%d %b %Y')
        tasks_dict['due_date'].append(due_date)

        completion = ' '.join(list[5].split())
        tasks_dict['completion'].append(completion)

while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input(f'''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        
        print(f"\nRegistering a user")

        # Prompt user to input new user and password
        new_user = input("Enter a new user: ")
        new_password = input("Enter a new password: ")

        # Confirm password input:
        # If true continue and append user and password into user file
        # Elif false, prompt user passwords do not match
        confirm_password = input("Please confirm password, enter the password again: ")

        if new_password == confirm_password:
            print("Password confirmed")
            
            with open('./user.txt', 'a') as user_file:
                user_file.write(f"{new_user}, {confirm_password}\n")
                print("User added.")

        elif new_password != confirm_password:
            print("Passwords do not match. New user not added.")

    elif menu == 'a':
        
        print(f"\nAdding a task")

        # User to input task data
            #   - user, 
            #   - task, 
            #   - task description, 
            #   - issue date (required to be converted into datetime convention and auto assigned to today's date)  
            #   - due date (required to be converted into datetime convention)
            #   - completion (auto assigned to 'No')
        user = input("Enter the username of the person whom the task is assigned to: ").lower()
        task = input("Enter the title of the task: ")
        task_descr = input("Enter the description of the task: ")
        issue_date = datetime.today().date()
        issue_date = issue_date.strftime("%d %b %Y")        
        due_date = input("Enter the due date of the task in the form 'DD MMM YYYY': ")
        due_date = datetime.strptime(due_date, "%d %b %Y")
        due_date = due_date.strftime("%d %b %Y")
        completion = 'No'

        # Append task data into tasks file
        with open('./tasks.txt', 'a') as tasks_file:
            tasks_file.write(f"\n{user}, {task}, {task_descr}, {issue_date}, {due_date}, {completion}")
            print("Tasks added.")

    if menu == 'va':

        print("\nView all tasks")

        # Print all values from the tasks dictionary with the following keys:
            #   - user, 
            #   - task, 
            #   - task description, 
            #   - issue date, 
            #   - due date, 
            #   - completion
        for (user), (task), (issue_date), (due_date), (completion), (task_descr) in zip(tasks_dict['user'], tasks_dict['task'], tasks_dict['issue_date'], tasks_dict['due_date'], tasks_dict['completion'], tasks_dict['task_descr']):
            
            print("_"*100 + "\n")

            print(f'''Task:\t\t\t{task}
Assigned to:\t\t{user}
Date assigned:\t\t{issue_date.strftime("%d %b %Y")}
Due date:\t\t{due_date.strftime("%d %b %Y")}
Task Complete:\t\t{completion}
Task description:\t{task_descr}''')

            print("_"*100 + "\n")

    elif menu == 'vm':

        print("View my task.")

        # Print values from the tasks dictionary with the following keys:
            #   - user, 
            #   - task, 
            #   - task description, 
            #   - issue date, 
            #   - due date, 
            #   - completion 
        # where user is equal to the user logged in.
        for (user), (task), (issue_date), (due_date), (completion), (task_descr) in zip(tasks_dict['user'], tasks_dict['task'], tasks_dict['issue_date'], tasks_dict['due_date'], tasks_dict['completion'], tasks_dict['task_descr']):
            
            if user == user_input:

                print("_"*100 + "\n")

                print(f'''Task:\t\t\t{task}
Assigned to:\t\t{user}
Date assigned:\t\t{issue_date.strftime("%d %b %Y")}
Due date:\t\t{due_date.strftime("%d %b %Y")}
Task Complete:\t\t{completion}
Task description:\t{task_descr}''')

                print("_"*100 + "\n")

    # Exit program when 'e' has been entered
    elif menu == 'e':

        print('Goodbye!!!')
        exit()
    
    # If menu input does not match one of the selected options
    # Prompt user to try again
    if menu not in ['r', 'a', 'va', 'vm','e']:

        print(f"\nYou have made a wrong choice, Please Try again.")
