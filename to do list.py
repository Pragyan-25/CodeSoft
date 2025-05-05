tasks = []
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{index}. {task['title']} [{status}]")

def add_task():
    title = input("Enter the task: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def mark_task_done():
    show_tasks()
    try:
        number = int(input("Enter the task number to mark as done: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        number = int(input("Enter the task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    show_menu()
    choice = int(input("Choose an option (1-5): "))

    match choice:
         case 1:
            show_tasks()
         case 2:
            add_task()
         case 3:
            mark_task_done()
         case 4:
            delete_task()
         case 5:
            print("GoodBye!")
            break
         case default:
             print("Invalid option!")
       
            
