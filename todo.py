from datetime import datetime

tasks = []

while True:
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Statistics")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter task: ")
        priority = input("Priority (High/Medium/Low): ")

        tasks.append({
            "task": task,
            "priority": priority,
            "completed": False,
            "created": datetime.now().strftime("%d-%m-%Y %H:%M")
        })

        print("✅ Task added successfully!")

    elif choice == "2":

        if not tasks:
            print("No tasks available.")

        else:
            print("\n----- TASK LIST -----")

            for i, item in enumerate(tasks, start=1):

                status = "✔ Completed" if item["completed"] else "⏳ Pending"

                print(
                    f"{i}. {item['task']} | {item['priority']} | {status} | {item['created']}"
                )

    elif choice == "3":

        if not tasks:
            print("No tasks available.")

        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                task_num = int(input("Enter task number: "))

                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("✅ Task marked as completed!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "4":

        if not tasks:
            print("No tasks available.")

        else:
            for i, item in enumerate(tasks, start=1):
                print(f"{i}. {item['task']}")

            try:
                task_num = int(input("Enter task number to delete: "))

                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑 Deleted: {removed['task']}")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("❌ Please enter a valid number.")

    elif choice == "5":

        keyword = input("Enter task name to search: ").lower()

        found = False

        for item in tasks:
            if keyword in item["task"].lower():
                status = "✔ Completed" if item["completed"] else "⏳ Pending"
                print(f"{item['task']} | {status}")
                found = True

        if not found:
            print("Task not found.")

    elif choice == "6":

        total = len(tasks)
        completed = sum(1 for task in tasks if task["completed"])
        pending = total - completed

        print("\n===== TASK STATISTICS =====")
        print("Total Tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)

    elif choice == "7":

        print("\n===== FINAL REPORT =====")

        for item in tasks:
            status = "Completed" if item["completed"] else "Pending"
            print(f"{item['task']} - {status}")

        print("👋 Exiting To-Do List...")
        break

    else:
        print("❌ Invalid choice. Try again.")