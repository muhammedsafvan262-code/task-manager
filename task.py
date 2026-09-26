tasks =[]
import json
def show_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. complete task")
    print("4. delete task")
    print("5. Exit")

def add_task():
    while True:
     task = input("Enter your task: ")
     new_task = {
       "task":task,
       "completed":False
     }
     tasks.append(new_task)
     save_tasks()
     print("Task added successfully!")

     again=input("do you want to add another task(y/n):")
     if again.lower() !="y":
        return
    

def view_task():
 if not tasks:
    print("no tasks available")
 else:
    print("tasks available:")
    for number,task in enumerate(tasks, start=1):
       print(number, task["task"])
       if task["completed"]:
          print("Status: Completed")
       else:
            print("Status: Not Completed") 


def complete_task():
    if not tasks:
        print("No tasks available to complete.")
        return
    view_task()
    task_number = int(input("Enter the task number to mark as completed: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks()
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task():
    if not tasks:
        print("sorry not task available to delete.")
        return
    view_task()
    task_number= int(input("enter your task number to delete"))
    if 1<=task_number<=len(tasks):
        deleted_task=tasks.pop(task_number-1)
        save_tasks()
        print("deleted",deleted_task["task"])

def save_tasks():
     with open("tasks.json","w")as file:
          json.dump(tasks,file)
def load_tasks():
     global tasks

     try:
      with open("tasks.json","r") as file:
          tasks = json.load(file)
     except FileNotFoundError:
          tasks = []

load_tasks()

while True:
    show_menu()
    choice=int(input("Enter your choice: "))
    if choice==1:
            add_task() 
    elif choice==2:
            view_task()
    elif choice==3:
            complete_task()
    elif choice==4:
            delete_task()
    elif choice==5:
            print("exitingggg the programme")
            break

    else:
         print("invalid chocie,,,,,,,...")

                     

    

    

        


        


