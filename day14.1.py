def display_tasks():
    try:
        with open("tasks.txt" , "r")as file:
            tasks=file.readlines()
            if not tasks:
                print("No tasks available")
            else:
                print("your tasks:")
                for index,task in enumerate(tasks,start=1):
                    print(f"{index}.{task.strip()}")
    except FileNotFoundError:
        print("No tasks found.start by adding new tasks")

def add_task():
    task=input("enter a new task:")
    with open("tasks.txt","a")as file:
        file.write(task + "\n")
        print("Tasks added sucessfully")

def remove_task():
    display_tasks()
    try:
        with open("tasks.txt","r")as file:
            tasks=file.readlines()
            if not tasks:
                return
            task_num=int(input("Enter the task number to remove:"))
            if 1<=task_num <=len(tasks):
                del tasks[task_num -1]
                with open("tasks.txt" ,"w") as file:
                    file.writelines(tasks)
                    print("Task removed sucessfully")
            else:
                print("Invalid task number")
    except ValueError:
        print("please enter a valid number")

while True:
    print("\n To-Do List")
    print("1.View Tasks")
    print("2. Add Task")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
      display_tasks()
    elif choice == "2":
      add_task()
    elif choice == "3":
      remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
     print("Invalid choice. Please try again.")
                            
