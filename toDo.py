def display_menu():
    print("To-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added.")

def remove_task(tasks):
    task_number = int(input("Enter the task number to remove: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task removed.")
    else:
        print("Invalid task number.")

def to_do_list():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

to_do_list()
