import os
tasks=[]
def menu():
    print("1. Add a Task")
    print("2. Show Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Exit")
def load_task():
     if os.path.exists("tasks.txt"):
        with open("tasks.txt","r") as file:
            for line in file:
                task,status=line.strip().split(":")
                tasks.append({task:status})
def save_tasks():
    with open ("tasks.txt","w") as file:
        for task_dict in tasks:
            for task,status in task_dict.items():
                file.write(f"{task}:{status}\n")
                     
def add_task(task):
    tasks.append({task:"Pending"})
    print("Task Added")
def show_task():
    if tasks:
        print("--------------TASKS------------")
        for i,task_dict in enumerate(tasks):
            for task,status in task_dict.items():
                print(f"{i+1}.{task}: {status}")
        print("\n")
    else:
        print("No task available")

def remove_task(task_no):
    if(task_no <= 0 or task_no>len(tasks)):
        print("Invalid Task Number!")
    else:
        tasks.pop(task_no)
        print("Task Removed Succesfully")

def update_task(task_no):
    if(task_no<=0 or task_no>len(tasks)):
        print("Invalid Task Number!")
    else:
        task_name=list(tasks[task_no].keys())[0]
        tasks[task_no][task_name]="Done"
        print("Task Marked as Done")
def main():
    load_task()
    while(True):
        menu()
        choice=int(input("Choose an Operation: "))
        if(choice==1):
            task=str(input("Enter Task Name: "))
            add_task(task)
        elif(choice==2):
            show_task()
        elif(choice==3):
            show_task()
            taskno=int(input("Enter the serial number of task to be removed: "))
            remove_task(taskno)
        elif(choice==4):
            show_task()
            taskno=int(input("Enter the serial number of task to mark as completed: "))
            update_task(taskno)
        elif(choice==5):
            save_tasks()
            break
        else:
            print("Invalid Choice")
            
main()