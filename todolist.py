import json

# Load tasks
try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except:
    tasks = []

# Save tasks
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    save_tasks()
    print("Task added!\n")

# View tasks
def view_tasks():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\n--- Your Tasks ---")
        for i, t in enumerate(tasks):
            print(f"{i+1}. {t['task']} [{t['status']}]")
        print()

# Mark as done
def mark_done():
    view_tasks()
    num = int(input("Enter task number to mark as done: "))
    if 0 < num <= len(tasks):
        tasks[num-1]["status"] = "Done"
        save_tasks()
        print("Task marked as completed!\n")
    else:
        print("Invalid number\n")

# Delete task
def delete_task():
    view_tasks()
    num = int(input("Enter task number to delete: "))
    if 0 < num <= len(tasks):
        tasks.pop(num-1)
        save_tasks()
        print("Task deleted!\n")
    else:
        print("Invalid number\n")

# Menu
while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice\n")