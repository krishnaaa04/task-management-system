from manager.task_manager import TaskManager

def print_menu():
    """
    Displays the main menu options for the CLI Task Management System.
    """
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
    """
    Main function to run the CLI-based task manager.
    Handles user input and performs corresponding operations.
    """
    task_manager = TaskManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-10): ")

        try:
            if choice == "1":
                user_id = int(input("Enter User ID: "))
                name = input("Enter name: ").strip()
                email = input("Enter email: ").strip()
                task_manager.create_user(user_id, name, email)

            elif choice == "2":
                task_id = int(input("Enter Task ID: "))
                title = input("Enter title: ").strip()
                description = input("Enter description: ").strip()
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                priority = input("Enter priority (Low, Medium, High): ").strip().capitalize()
                task_manager.create_task(task_id, title, description, due_date, priority)

            elif choice == "3":
                task_id = int(input("Enter Task ID: "))
                user_id = int(input("Enter User ID to assign task: "))
                task_manager.assign_task_to_user(task_id, user_id)

            elif choice == "4":
                task_id = int(input("Enter Task ID: "))
                new_status = input("Enter new status (To Do, In Progress, Done): ").strip().title()
                task_manager.update_task_status(task_id, new_status)

            elif choice == "5":
                task_id = int(input("Enter Task ID: "))
                new_priority = input("Enter new priority (Low, Medium, High): ").strip().capitalize()
                task_manager.update_task_priority(task_id, new_priority)

            elif choice == "6":
                task_id = int(input("Enter Task ID to delete: "))
                task_manager.delete_task(task_id)

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
                    print("No tasks found for this user.")

            elif choice == "9":
                status = input("Enter status to filter (To Do, In Progress, Done): ").strip().title()
                tasks = task_manager.list_tasks_by_status(status)
                if tasks:
                    for task in tasks:
                        print(task)
                        print("-" * 40)
                else:
                    print("No tasks with this status.")

            elif choice == "10":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")
        except ValueError as ve:
            print("Input Error:", ve)
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
