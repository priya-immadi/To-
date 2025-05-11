import os

# Task list stored in a simple list
tasks = []

# Function to display the task list
def show_tasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{idx}. {task['task']} - {status}")

# Function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added!")

# Function to remove a task
def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid task number.")

# Function to mark a task as completed
def complete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 0 < task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print(f"Task '{tasks[task_num - 1]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid task number.")

# Function to show menu options
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark task as completed")
    print("5. Exit")

# Main function to run the application
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()
