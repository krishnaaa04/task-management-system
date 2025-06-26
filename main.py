from manager.task_manager import TaskManager

def print_menu():
    print("\n--- Task Management System ---")
    print("1. Create User")
    print("2. Create Task")
    print("3. Assign Task to User")
    print("4. Update Task Status")
    print("5. Update Task Priority")
    print("6. Delete Task")
    print("7. View All Tasks")
    print("8. View Tasks by User")
    print("9. View Tasks by Status")
    print("10. Exit")

def main():
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            user_id = int(input("Enter User ID: "))
            name = input("Enter name: ")
            email = input("Enter email: ")
            task_manager.create_user(user_id, name, email)
            print(" User created.")

        elif choice == "2":
            task_id = int(input("Enter Task ID: "))
            title = input("Enter title: ")
            description = input("Enter description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low, Medium, High): ")
            task_manager.create_task(task_id, title, description, due_date, priority)
            print(" Task created.")

        elif choice == "3":
            task_id = int(input("Enter Task ID: "))
            user_id = int(input("Enter User ID to assign task: "))
            task_manager.assign_task_to_user(task_id, user_id)
            print(" Task assigned.")

        elif choice == "4":
            task_id = int(input("Enter Task ID: "))
            new_status = input("Enter new status (To Do, In Progress, Done): ")
            task = task_manager.get_task(task_id)
            if task:
                task.update_status(new_status)
                print("Status updated.")
            else:
                print(" Task not found.")

        elif choice == "5":
            task_id = int(input("Enter Task ID: "))
            new_priority = input("Enter new priority (Low, Medium, High): ")
            task = task_manager.get_task(task_id)
            if task:
                task.update_priority(new_priority)
                print(" Priority updated.")
            else:
                print("Task not found.")

        elif choice == "6":
            task_id = int(input("Enter Task ID to delete: "))
            task_manager.delete_task(task_id)
            print("Task deleted if it existed.")

        elif choice == "7":
            print("\n--- All Tasks ---")
            for task in task_manager.list_all_tasks():
                print(task)
                print("-" * 40)

        elif choice == "8":
            user_id = int(input("Enter User ID: "))
            tasks = task_manager.list_tasks_by_user(user_id)
            if tasks:
                for task in tasks:
                    print(task)
                    print("-" * 40)
            else:
                print(" No tasks found for this user.")

        elif choice == "9":
            status = input("Enter status to filter (To Do, In Progress, Done): ")
            tasks = task_manager.list_tasks_by_status(status)
            if tasks:
                for task in tasks:
                    print(task)
                    print("-" * 40)
            else:
                print(" No tasks with this status.")

        elif choice == "10":
            print(" Exiting... Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
