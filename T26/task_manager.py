#=====importing libraries===========
from datetime import datetime
import operator
import os.path

#====Login Section====

# Open user.txt and store user login information as a dictionary
with open('C:/Users/erwin/OneDrive/Documents/DfE HyperionDev/Software Engineering/T26/user.txt', 'r') as user_file:

    #Create empty dict to store user login information
    login_dict = {}

    # For each new line in user file, split line into elements
    # Assigning first element 'user' as key
    # and second element 'password' as value 
    for line in user_file:
        login_list = line.split(', ')
        login_dict[login_list[0]] = ''.join(login_list[1].split())

# Prompt user for username
# If username exists, break loop
# Else loop
while True:

    user_input = input("Enter username: ")

    if user_input in login_dict.keys():
        break
    
    else:
        print("Username not found. Try again.\n")


# Prompt user for password (for selected user)
# If password is correct for user, break loop
# Else loop
while True:

    password_input = input("Enter password: ")

    if password_input == login_dict[user_input]:
        break
    
    else:
        print("Password is incorrect. Try again.\n")
        
# Prompt user has logged in.
print(f"Hi {user_input}, you have successfully logged in.")

# Open tasks.txt and store task information as a dictionary
with open('C:/Users/erwin/OneDrive/Documents/DfE HyperionDev/Software Engineering/T26/tasks.txt', 'r') as tasks_file:

    # Create empty dictionaries following tasks_file format
    # tasks_dict used as main retrieval and updating
    tasks_dict = {
        'user':[],
        'task_id':[],
        'task':[],
        'task_descr':[],
        'issue_date':[],
        'due_date':[],
        'completion':[]
        }

    # For each line in tasks append the following keys:
    #   - user, 
    #   - task_id (= {user}_{idx})
    #   - task, 
    #   - task description, 
    #   - issue date, 
    #   - due date, 
    #   - completion 
    # into the dictionary. Note, values stored as a list
    for idx, line in enumerate(tasks_file):
        task_list = line.split(', ')
        
        user = ' '.join(task_list[0].split())
        tasks_dict['user'].append(user)
        
        tasks_dict['task_id'].append(user + '_' + str(idx))

        task = ' '.join(task_list[1].split())
        tasks_dict['task'].append(task)

        task_descr = ' '.join(task_list[2].split())
        tasks_dict['task_descr'].append(task_descr)

        # Note: dates convert from string inputs to conventional date format DD MMM YYYY
        issue_date = ' '.join(task_list[3].split())
        issue_date = datetime.strptime(issue_date, '%d %b %Y')
        tasks_dict['issue_date'].append(issue_date)

        due_date = ' '.join(task_list[4].split())        
        due_date = datetime.strptime(due_date, '%d %b %Y')
        tasks_dict['due_date'].append(due_date)

        completion = ' '.join(task_list[5].split())
        tasks_dict['completion'].append(completion)

    # Create empty dict to store user's tasks
    # Used for generate report and statistics
    user_tasks_dict = {
        'user':[],
        'task_id':[],
        'task':[],
        'task_descr':[],
        'issue_date':[],
        'due_date':[],
        'completion':[]
        }
    
    # Append values into user_tasks_dict
    # Where user is set to the user_input
    for (user), (task), (task_id), (issue_date), (due_date), (completion), (task_descr) in zip(tasks_dict['user'], tasks_dict['task'], tasks_dict['task_id'], tasks_dict['issue_date'], tasks_dict['due_date'], tasks_dict['completion'], tasks_dict['task_descr']):
            
            if user == user_input:
                
                user_tasks_dict['user'].append(user)
                user_tasks_dict['task'].append(task)
                user_tasks_dict['task_id'].append(task_id)
                user_tasks_dict['task_descr'].append(task_descr)
                user_tasks_dict['issue_date'].append(issue_date)
                user_tasks_dict['due_date'].append(due_date)
                user_tasks_dict['completion'].append(completion)
        
                
#====Function Section====

def reg_user():

    print(f"\nRegistering a user")

    # Prompt user to input new user
    # If user exists, prompt user and ask again to reenter new user
    # Else break loop
    while True:
        
        new_user = input("Enter a new user: ")

        if new_user in login_dict.keys():
            print("User exists, please enter new user.")
        
        else:
            break


    # Prompt user for new password and confirmation
    # If true continue and append user and password into user file
    # Elif false, prompt user passwords do not match
    new_password = input("Enter a new password: ")
    confirm_password = input("Please confirm password, enter the password again: ")

    if new_password == confirm_password:
        print("Password confirmed")
        
        with open('./user.txt', 'a') as user_file:
            user_file.write(f"{new_user}, {confirm_password}\n")
            print("User added.")

    elif new_password != confirm_password:
        print("Passwords do not match. New user not added. Returning to menu.")
    

def add_task():

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
        tasks_file.write(f"{user}, {task}, {task_descr}, {issue_date}, {due_date}, {completion}\n")
        print("Tasks added.")


def view_all():

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


def view_mine():

    print("\nView my task")

    # Print all user's incomplete tasks
    # Where user is given by the user_input 
    # AND where completion is equal to 'No'
    print(f"\n{user_input}'s incomplete tasks:")
    
    for (user), (task_id), (completion) in zip(tasks_dict['user'], tasks_dict['task_id'], tasks_dict['completion']):
        
        if user == user_input and completion == 'No':
            
            print(f"\t- {task_id}")
    
    # Print all user's completed tasks
    # Where user is given by the user_input 
    # AND where completion is equal to 'Yes'
    print(f"\n{user_input}'s completed tasks:")

    for (user), (task_id), (completion) in zip(tasks_dict['user'], tasks_dict['task_id'], tasks_dict['completion']):
        
        if user == user_input and completion == 'Yes':
            print(f"\t- {task_id}")

    # Prompt user to enter task id number 
    select_task = input(f"\nEnter task_id to view or enter '-1' to return to menu: ")

    # Open task where task_id matches value in dictionary
    if select_task in tasks_dict['task_id']:

        # Get index of task_id from tasks_dict
        idx = tasks_dict['task_id'].index(select_task)

        # Print values from the tasks_dict with the following keys:
            #   - task index number (note starts from 0),
            #   - user,
            #   - task, 
            #   - task description, 
            #   - issue date, 
            #   - due date, 
            #   - completion
        # Where index is given by the task_id
        print("_"*100 + "\n")
        print(f'''Task ID:\t\t{tasks_dict['task_id'][idx]}
Assigned to:\t\t{tasks_dict['user'][idx]}
Task:\t\t\t{tasks_dict['task'][idx]}
Date assigned:\t\t{tasks_dict['issue_date'][idx].strftime("%d %b %Y")}
Due date:\t\t{tasks_dict['due_date'][idx].strftime("%d %b %Y")}
Task Complete:\t\t{tasks_dict['completion'][idx]}
Task description:\t{tasks_dict['task_descr'][idx]}''')
        print("_"*100 + "\n")

        # Open viewn mine menu for the following options:
        # Mark task as complete - change completion to yes
        # Edit the task - change task assignee and due date
        view_mine_menu = input(f'''\nSelect one of the following Options below:
mk - Mark the task as complete
ed - Edit the task
: ''').lower()

        if view_mine_menu == 'mk':
            
            # If selected task completion already set to 'Yes'
            # Return back to main menu
            if tasks_dict['completion'][idx] == 'Yes':
                print(f"{tasks_dict['task'][idx]} has already been marked completed.")
                return
            
            # Confirm user wishes to mark the task as complete
            ask_completion = input("Do you want to mark this task as complete: ").lower()
            
            # If task marked to be complete
            # Update tasks_dictionary and overwrite tasks.txt
            # Exit program to ensure overwrite has been completed
            if ask_completion == 'yes':
                tasks_dict['completion'][idx] = 'Yes'
                print(f"{tasks_dict['task'][idx]} marked complete")
                
                # Write tasks_dict to tasks.txt file
                with open('./tasks.txt', 'w') as tasks_file:
                    for (user), (task), (issue_date), (due_date), (completion), (task_descr) in zip(tasks_dict['user'], tasks_dict['task'], tasks_dict['issue_date'], tasks_dict['due_date'], tasks_dict['completion'], tasks_dict['task_descr']):
                        issue_date = issue_date.strftime("%d %b %Y")
                        due_date = due_date.strftime("%d %b %Y")
                        tasks_file.write(f"{user}, {task}, {task_descr}, {issue_date}, {due_date}, {completion}\n")
                
                print("tasks.txt updated. Now exitting program.")
                exit()

            # If task not complete
            # Return to main menu
            elif ask_completion == 'no':
                tasks_dict['completion'][select_task] = 'No'
                print(f"{tasks_dict['task'][select_task]} marked incomplete")
                return

            # If input not 'yes' or 'no
            # Prompt user input is invalid and return to view mine menu
            else:
                print("Input not recognised. Returning to menu.")
                view_mine()

        elif view_mine_menu == 'ed':

            # If selected task completion already set to 'Yes'
            # Prompt user that task cannot be editted and
            # Return back to main menu
            if tasks_dict['completion'][idx] == 'Yes':
                print(f"{tasks_dict['task'][idx]} has been marked complete. Task cannot be editted.")
                return
            
            # If task completion set to 'No'
            # Ask user to confirm making edits to task
            # if yes, make updates to 'user' and 'due_date'
            # Update tasks_dict and write to tasks.txt
            elif tasks_dict['completion'][idx] == 'No':
                print(f"{tasks_dict['task'][idx]} has been marked incomplete.")

                # Confirm user to update task
                ask_update = input("Do you wish to update this task: ").lower()
                
                # If yes, prompt user for new assigned user and due date for task
                # Update tasks_dict and overwrite tasks.txt
                # Exit program to ensure overwrite has been completed
                if ask_update == 'yes':
                        
                    user = input("Enter new assigned user: ")
                    due_date = input("Enter new due date of the task in the form 'DD MMM YYYY': ")
                    due_date = datetime.strptime(due_date, "%d %b %Y")
                    tasks_dict['user'][idx] = user
                    tasks_dict['due_date'][idx] = due_date

                    # Write tasks_dict to tasks.txt file
                    with open('./tasks.txt', 'w') as tasks_file:
                        for (user), (task), (issue_date), (due_date), (completion), (task_descr) in zip(tasks_dict['user'], tasks_dict['task'], tasks_dict['issue_date'], tasks_dict['due_date'], tasks_dict['completion'], tasks_dict['task_descr']):
                            issue_date = issue_date.strftime("%d %b %Y")
                            due_date = due_date.strftime("%d %b %Y")
                            tasks_file.write(f"{user}, {task}, {task_descr}, {issue_date}, {due_date}, {completion}\n")
                    
                    print("tasks.txt updated. Now exitting program.")
                    exit()

                # If edit not required
                # Return to main menu
                elif ask_update == 'no':
                    print(f"{tasks_dict['task'][idx]} has not been updated.")
                    return
                
                 # If input not 'yes' or 'no'
                # Prompt user input is invalid and return to view mine menu
                else:
                    print("Input not recognised. Returning to menu.")
                    view_mine()
                    return

            # If input not 'mk' or 'ed'
            # Prompt user input is invalid and return to view mine menu
            else:
                print("Input not recognised. Returning to menu.")
                view_mine()
        
        # If input not 'mk' or 'ed'
        # Prompt user input is invalid and return to view mine menu
        else:
            print("Input not recognised. Returning to menu.")
            view_mine()
    
    # Return to main menu
    elif select_task == '-1':
        print("Returning to menu.")
        return
    
    # If input did not match task_id or '-1'
    # Prompt user input is invalid and return to view mine menu
    else:
        print("Option not available. Try again.")
        view_mine()


def generate_report():

    print("\nGenerate Reports")

    # The total number of tasks that have been generated and tracked using task_manager
    total_tasks = len(tasks_dict['task'])

    # Total of completed tasks
    total_completed_tasks = operator.countOf(tasks_dict['completion'], 'Yes')

    # Total of uncompleted tasks
    total_uncomplete_tasks = (operator.countOf(tasks_dict['completion'], 'No'))

    # Total number of tasks not complete and overdue
    # only count when task completion is set to 'No'
    # Increment count where due date < today's date 
    total_overdue_tasks = 0
    for (completion), (due_date) in zip(tasks_dict['completion'], tasks_dict['due_date']):
        if completion == 'No':
            if due_date.date() < datetime.today().date():
                total_overdue_tasks = total_overdue_tasks + 1

    # % of tasks that are uncomplete
    total_percent_uncomplete_tasks = (total_uncomplete_tasks/total_tasks)*100

    # % of tasks that are overdue
    total_percent_overdue_tasks = (total_overdue_tasks/total_tasks)*100

    # Write task_overview.txt
    # Report task completion statistics
    with open('./task_overview.txt', 'w') as task_overview_file:
        task_overview_file.write(f'''Total number of tasks generated: {total_tasks}
Total number of completed tasks: {total_completed_tasks}
Total number of uncompleted tasks: {total_uncomplete_tasks}
Total number of overdue tasks: {total_overdue_tasks}
Percentage of overdue tasks: {total_percent_uncomplete_tasks}%
Percentage of overdue tasks: {total_percent_overdue_tasks}%''')  
        print("Task overview report generated.")

    # The number of user's tasks that have been generated and tracked using task_manager
    user_tasks = len(user_tasks_dict['task'])

    # User's completed tasks
    user_completed_tasks = operator.countOf(user_tasks_dict['completion'], 'Yes')

    # User's uncompleted tasks
    user_uncomplete_tasks = (operator.countOf(user_tasks_dict['completion'], 'No'))

    # Number of user's tasks not complete and overdue
    # only count when task completion is set to 'No'
    # Increment count where due date < today's date 
    user_overdue_tasks = 0
    for (completion), (due_date) in zip(user_tasks_dict['completion'], user_tasks_dict['due_date']):
        if completion == 'No':
            if due_date.date() < datetime.today().date():
                user_overdue_tasks = user_overdue_tasks + 1

    # % of user's tasks that are uncomplete
    user_percent_uncomplete_tasks = (user_uncomplete_tasks / user_tasks)*100

    # % of user's tasks that are overdue
    user_percent_overdue_tasks = (user_overdue_tasks / user_tasks)*100

    # Save file as user_overview
    with open(f'./user_overview.txt', 'w') as user_overview_file:
        user_overview_file.write(f'''{user_input}'s number of tasks generated: {user_tasks}
{user_input}'s number of completed tasks: {user_completed_tasks}
{user_input}'s number of uncompleted tasks: {user_uncomplete_tasks}
{user_input}'s number of overdue tasks: {user_overdue_tasks}
Percentage of {user_input}'s uncomplete tasks: {user_percent_uncomplete_tasks}%
Percentage of {user_input}'s overdue tasks: {user_percent_overdue_tasks}%''')  
    print("User overview report generated.")


def display_statistics():
    
    # Run generate report function 
    # If files 'task_overview.txt' and 'user_overview.txt' don't exist
    file_exists = os.path.exists('task_overview.txt') and os.path.exists('user_overview.txt')
    if file_exists is False:
        generate_report()  

    # Open 'task_overview.txt'
    # Print file
    with open('./task_overview.txt', 'r') as task_overview_file:
        
        print("\nDisplay statistics - All tasks")
        print(task_overview_file.read())

    # Open 'user_overview.txt'
    # Print file
    with open(f'./user_overview.txt', 'r') as user_overview_file:
        
        print(f"\nDisplay statistics - {user_input}'s tasks")
        print(user_overview_file.read())


#====Menu Section====


while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    # When option is selected - run designated function.
    menu = input(f'''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
       
    elif menu == 'a':
        add_task()

    if menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        generate_report()

    elif menu == 'ds':
        display_statistics()
        
    # Exit program when 'e' has been entered
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    # If menu input does not match one of the selected options
    # Prompt user to try again
    if menu not in ['r', 'a', 'va', 'vm', 'gr', 'ds','e']:
        print(f"\nYou have made a wrong choice, Please Try again.")
