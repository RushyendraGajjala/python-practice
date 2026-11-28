import json
import csv
import os
FILE_NAME = "tasks.txt"

def load_tasks():
    tasks = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                task_id, title, status, priority = line.strip().split(" | ", 3)
                tasks[int(task_id)] = {"title" : title, "status": status, "priority": priority}
    return tasks

def export_json(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

    print("Tasks exported successfully!")

def export_csv(tasks):
    with open("tasks.csv", "w", newline="") as f:
        fieldnames = ["task_id", "title", "status", "priority"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for task_id, task in tasks.items():
            writer.writerow({
                "task_id": task_id,
                "title": task["title"],
                "status": task["status"],
                "priority": task["priority"]
            })
    print("Exported CSV_File")

def add_priority(tasks):
    print("Priority options: na/ low/ avg/ high")
    task_id = int(input("Enter the task id to mark the priority: "))
    if task_id in tasks:
        while True:
            priority = input("Enter the priority for task: ").lower()
            if priority in ["low", "avg", "high", "na"]:
                tasks[task_id]['priority'] = priority
                break
            else:
                print("Enter within valid priority: na/ low/ avg/ high\n")


def save_task(tasks):
    with open(FILE_NAME, "w") as f:
        for task_id, task in tasks.items():
            f.write(f"{task_id} | {task['title']} | {task['status']} | {task['priority']}\n")


def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title" : title, "status" : "incomplete", "priority": "NA"}
    save_task(tasks)
    print(f"task: '{title}' added")

def view_task(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id} : {task['title']} - {task['status']} | Priority: {task['priority']}]")

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
        print("5. Add Priority")
        print("6. Export Tasks as JSON")
        print("7. Export Tasks as CSV")
        print("8. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            task_completed(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            add_priority(tasks)
        elif choice == 6:
            export_json(tasks)
        elif choice == 7:
            export_csv(tasks)
        elif choice == 8:
            save_task(tasks)
            print("GoodByee:)")
            break
        else:
            print("Invalid choice please try again!")

if __name__ == "__main__":
    main()