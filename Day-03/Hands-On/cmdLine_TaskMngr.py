import os
FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                task_id, title, status = line.strip().split(" | ", 2)
                tasks[int(task_id)] = {"title" : title, "status": status}
    return tasks

def save_task(tasks):
    with open(FILE_NAME, "w") as f:
        for task_id, task in tasks.items():
            f.write(f"{task_id} | {task['title']} | {task['status']}\n")


def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title" : title, "status" : "incomplete"}
    save_task(tasks)
    print(f"task: '{title}' added")

def view_task(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id} : {task['title']} - {task['status']}]")

def task_completed(tasks):
    task_id = int(input("Enter the task id to mark it complete: "))
    if task_id in tasks:
        tasks[task_id]['status'] = "completed"
        print(f"Task {tasks[task_id]['title']} marked as complete")
    else:
        print("Task ID not found!")

def delete_task(tasks):
    task_id = int(input("Enter the task id to delete it: "))
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        print(f"Task \"{deleted_task['title']}\" is Removed!")
    else:
        print("Task ID not found!")

def main():
    tasks = load_tasks()
    while True:
        print("\n")
        print("1. Add task")
        print("2. View Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            task_completed(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            save_task(tasks)
            print("GoodByee:)")
            break
        else:
            print("Invalid choice please try again!")

if __name__ == "__main__":
    main()