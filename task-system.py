import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def add_task(tasks):
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = input("Enter priority (high, medium, low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    new_task = {
        'name': name,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} - Priority: {task['priority']} - Due Date: {task['due_date']}")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        task = tasks[task_index]

        new_description = input("Enter new description (leave blank to keep current): ")
        new_priority = input("Enter new priority (leave blank to keep current): ")
        new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")

        if new_description:
            task['description'] = new_description
        if new_priority:
            task['priority'] = new_priority
        if new_due_date:
            task['due_date'] = new_due_date

        save_tasks(tasks)
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{task['name']}' deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()