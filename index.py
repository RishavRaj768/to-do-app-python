# To Do app
import os

FILE_NAME = "tasks.txt"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


# View tasks
def view_tasks(tasks):
    if not tasks:
        print(" No tasks available.")
        return

    print("\n Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


# Delete task
def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed}")

    except (ValueError, IndexError):
        print(" Invalid task number!")


# Main Program
tasks = load_tasks()

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")