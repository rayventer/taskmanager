#=====importing libraries===========
from datetime import datetime
from datetime import date
t = date.today()

def reg_user():
    f = open('user.txt', 'a')
    username = input("Enter your username: ")
    password = input("Enter your password :")
    confirmation = input('confirm your password: ')
    users2 = open('user.txt', 'r', encoding='utf-8')
    lines2 = users2.readlines()
    user_exists = False

    for i in lines2:
        specifications = i.split(', ')
        #checks if user already exists
        if username == specifications[0].replace('\n', ''): 
            user_exists = True       

    if password == confirmation and user_exists == False: 
        #makes sure that only admin can register a user and registers the user by adding them to the text file
        f.write((f'\n{username}, {password}'))
    
    elif user_exists == False:
        print("This user already exists")
    
    else:
        print("Password and confirmed password aren't the same")
    f.close()


def add_task():
    ask_user = input("Enter the username of the person who should do this task: ")
    task_title = input("Enter the title of the task: ")
    task_description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task in the day month year format: ")
    task_app = open('tasks.txt', 'a')
    t = datetime.today()
    time = t.strftime('%d %B %Y')
    #takes all the user input and adds it to the text file without overwriting previous information
    task_app.write(f'{ask_user}, {task_title}, {task_description}, {time}, {due_date},  No \n' ) 
    task_app.close()


def view_all():
    #opens and reads from tasks
    va = open('tasks.txt', 'r', encoding='utf-8') 
    lines = va.readlines()
    for i in lines:
        specifications = i.split(', ')
        print('─' * 60)
        print(f'\nTask: \t\t{specifications[1]} \nAssigned to: \t{specifications[0]} \nDate assigned: \t{specifications[3]} \nDue date: \t{specifications[4]} \nTask complete?: {specifications[5]} \nTask description:\n {specifications[2]} \n')
        print('─' * 60) 
        #prints the data in the correct format
    va.close()


def view_mine():
    vm = open('tasks.txt', 'r', encoding='utf-8')
    lines = vm.readlines()
    task_num = 0
    number_of_tasks=0
    known_tasks = []
    for i in lines: 
        number_of_tasks +=1       
        specifications = i.split(', ')
        if specifications[0] == username:
            task_num+=1
            print('─' * 60)
            print(f'\n\nTask: \t\t{task_num} {specifications[1]} \nAssigned to: \t{specifications[0]} \nDate assigned: \t{specifications[3]} \nDue date: \t{specifications[4]} \nTask complete?: {specifications[5]} \nTask description:\n {specifications[2]} \n')
            print('─' * 60) 
            #finds the tasks of said user and prints them in an appropriate format
            known_tasks.append(i)
    if task_num == 0:
        print('You do not have any tasks.')
    else:
        user_task_check = input('do you want to edit a task or mark a task as complete? Y/N')
        if user_task_check == 'Y':
            check_task_status = input('''do you want to edit the task or mark it as complete?
            1-mark it as complete
            2-edit the task
            3-Go back to main menu''') 
            # checks with user if they want to mark a task as complete
            if check_task_status == '1':
                task_edited = int(input('Enter the task number you want to edit or mark as completed: '))
                specific_task = known_tasks[task_edited-1].split(', ')
                taskapp = open('tasks.txt', 'r')
                lines = taskapp.readlines()
                lines[task_edited-1] = (f'{specific_task[0]}, {specific_task[1]}, {specific_task[2]}, {specific_task[3]}, {specific_task[4]},  Yes \n' ) #takes all the user input and adds it to the text file without overwriting previous information
                taskapp.close()
                task_app = open('tasks.txt', 'w')
                task_app.writelines(lines)
            elif check_task_status == '2':
                task_edited = int(input('Enter the task number you want to edit or mark as completed: '))
                specific_task = known_tasks[task_edited-1].split(', ')
                value_changed = input('''Select one of the following options below:
                                    1 to change the due date 
                                    2 to change the person to whom the task is assigned''') 
                if value_changed == '1':
                    duedate = input("Enter the due date")
                    taskapp = open('tasks.txt', 'r')
                    lines = taskapp.readlines()
                    lines[task_edited-1] = (f'{specific_task[0]}, {specific_task[1]}, {specific_task[2]}, {specific_task[3]}, {duedate},  {specific_task[5]}\n' ) #takes all the user input and adds it to the text file without overwriting previous information
                    taskapp.close()
                    task_app = open('tasks.txt', 'w')
                    task_app.writelines(lines)
                elif value_changed == '2':
                    changeduser = input("Enter the user")
                    taskapp = open('tasks.txt', 'r')
                    lines = taskapp.readlines()
                    lines[task_edited-1] = (f'{changeduser}, {specific_task[1]}, {specific_task[2]}, {specific_task[3]}, {specific_task[4]},  {specific_task[5]}\n' ) #takes all the user input and adds it to the text file without overwriting previous information
                    taskapp.close()
                    task_app = open('tasks.txt', 'w')
                    task_app.writelines(lines)
                            

    vm.close() 


def generate_reports():
    f1 = open('task_overview.txt', 'w', encoding='utf-8')
    f2 = open('user_overview.txt', 'w')
    vm = open('tasks.txt', 'r', encoding='utf-8')
    vy = open('user.txt', 'r', encoding ='utf-8')
    lines = vm.readlines()
    task_num = 0
    number_of_tasks = 0
    no_completed = 0
    no_notcompleted = 0
    users = 0
    users_task_completed = []
    userstaskincompleted = []
    overduetasks = []
    appearance_list = []
    nooverdue = 0 
    
    for i in lines: 
        number_of_tasks+=1  
        specifications = i.split(', ')
        usernamus = specifications[0]
        appearance_list.append(usernamus)
        task_num+=1
        if specifications[5].replace('\n', '').strip() == 'Yes':
            #tallies amount of completed tasks
            no_completed+=1 
            users_task_completed.append(specifications[0])
        elif specifications[5].replace('\n', "").strip() == 'No': 
            #tallies uncompleted tasks
            userstaskincompleted.append(usernamus)
            no_notcompleted+=1 
            try:
                duedate = datetime.strptime(specifications[4], '%d %b %Y')
            except Exception:
                duedate = datetime.strptime(specifications[4], '%d %B %Y')
            today = datetime.today()
            #checks if the tasks due date has been passed and appends it to a list which length will be counted to give the total amount of incomplete tasks
            if today > duedate:
                usernamus = specifications[0]
                overduetasks.append(usernamus)
                print(usernamus)
                nooverdue+=1
                print(f'{nooverdue} {i}')


    incomplete_percentage = 100-(no_completed/task_num * 100)
    lines2 = vy.readlines()
    userslist = []
    tasklist = []

    for i in lines2:
        users+=1
        specifications2 = i.split(', ')
        username = specifications2[0]
        if username not in tasklist:
            userslist.append(username)
        tasklist.append(username)
    f2.write(f'The total amount of users is {users}\n\n')

    
    for i in userslist:
        task_count = appearance_list.count(i)
        if task_count !=0:
            completedcount = users_task_completed.count(i)
            overdue_count = (overduetasks.count(i)/task_count) * 100
            user_completed_percent = (completedcount/task_count) *100
            user_not_completed_percent = (1-completedcount/task_count) *100
            task_percent = task_count/number_of_tasks * 100
        else:
            completedcount = 0
            overdue_count = 0
            user_completed_percent = 0
            user_not_completed_percent = 0
            task_percent = 0
        f2.write('_' * 60 + f'\n {i} \nnumber of tasks: {task_percent} \nNumber of completed tasks: {completedcount} \nPercentage of completed tasks: {user_completed_percent}% \nPercent of incomplete tasks: {user_not_completed_percent}%\nPercent of overdue tasks: {overdue_count}%\n')    
    overdue_count = (nooverdue/number_of_tasks) *100
    f1.write('─' * 60 + f'\nTotal amount of tasks: {number_of_tasks} \nCompleted tasks: {no_completed} \nIncomplete tasks: {no_notcompleted}\nPercentage of incomplete tasks: {incomplete_percentage}% \nPercentage of overdue tasks: {overdue_count}% \n' + '─' * 60) 

def statistics():
    f1 = open('tasks.txt', 'r', encoding ='utf-8')
    f2 = open('user.txt', 'r', encoding='utf-8')
    generate_reports()
    tasks = open('task_overview.txt', 'r', encoding ='utf-8')
    lines1 = tasks.readlines()
    for i in lines1:
        print(i)
    usersover = open('user_overview.txt', 'r', encoding='utf-8')
    lines2 = usersover.readlines()
    for i in lines2:
        print(i)



#====Login Section====
users = open('user.txt', 'r', encoding='utf-8')
lines = users.readlines()
loggedin = False
while loggedin ==False:   
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    for i in lines:
        specifications = i.split(', ')
        if username == specifications[0].replace('\n', '') and password == specifications[1].replace('\n', ''):
            loggedin = True
    if loggedin == False:
        print('Incorrect password or username entered')




'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username != 'admin':
        menu = input('''Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - view statistics
gr - generate reports
e - Exit
: ''').lower()



    
    if menu == 'r' and username == 'admin':
        reg_user()
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        add_task()
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        view_all()  
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        view_mine()

                
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    elif menu =='ds':
        statistics()
    elif menu =='gr':
        generate_reports()

    else:
        print("You have made a wrong choice, Please Try again")