# now logic is completed in 31-jan-2026  6:48PM
#storing in csv file is completed in 21-feb-2026 3:57 pm
print("========================================================")
print("=================TO-DO APPLICATION======================")
print("========================================================")

import csv
tasks = []
def save_tasks():
    try:
        with open('tasks.csv', 'w', newline='') as csvfile:
        #fieldnames=['name','completed']
            writer=csv.DictWriter(csvfile,fieldnames=['Name','Status'])
            writer.writeheader()
            writer.writerows(tasks)
    except FileNotFoundError:
        print("File not found")


def load_tasks():
    try:
        with open('tasks.csv', 'r') as csvfile:
            csv_reader=csv.DictReader(csvfile)
            for row in csv_reader:
                tasks.append(row)
    except FileNotFoundError:
        print("File not found")

def add():
    task=input("Enter the task : ")
    tasks.append({'Name' : task,'Status' : 'Not Completed'})
    print("-------------------------")
    print(f"Task '{task}' has been added.")

def view():
    if not tasks:
        print("No task available")
    else:
        print("Your Tasks :")
        print("-------------------------")
        for i,task in enumerate(tasks,1):
            status= "[not completed]" if task['Status'] == 'Not Completed' else "[Completed]"
            print(f"{i}. {task['Name']} {status}")


def complete():
    if not tasks:
        print("No task available")
    else:
        view()
        n=int(input("Enter the task number to complete : "))
        if n >= 1 and n <= len(tasks):
            tasks[n-1]['Status']= 'Completed'
            print(f"{n}.{tasks[n-1]['Name']} completed.")
        else:
            print("Invalid task number")



def delete():
    if not tasks:
        print("No task available")
    else:
        view()
        n=int(input("Enter the task number to delete : "))
        if n >= 1 and n <= len(tasks):
            print(f"{n}.{tasks[n-1]['Name']} deleted.")
            tasks.pop(n-1)
        else:
            print("Invalid task number")

load_tasks()

while True:
    print("Select an Option")
    print("1.Add a task")
    print("2.View tasks")
    print("3.Mark a as Completed tasks")
    print("4.Delete a tasks")
    print("5.Exit")

    ch=int(input("Enter your choice = "))
    print("========================================================")

    if ch==1:
        add()
        save_tasks()
        print("========================================================")

    elif ch==2:
        view()
        print("========================================================")

    elif ch==3:
        complete()
        save_tasks()
        print("========================================================")

    elif ch==4:
        delete()
        save_tasks()
        print("========================================================")

    elif ch==5:
        print("Exit")
        break

    else:
        print("Invalid Choice")
        print("Please enter a number from 1 to 5")