class User:
    """
    Represents a user who can be assigned tasks.
    """

    def __init__(self, user_id, name, email):
        """
        Initializes a new User instance.
        """
        self.user_id = user_id
        self.name = name
        self.email = email
        self.task_list = []

    def add_task(self, task):
        """
        Adds a task to the user's task list.
        """
        self.task_list.append(task)

    def remove_task(self, task_id):
        """
        Removes a task from the user's task list based on task ID.
        """
        self.task_list = [task for task in self.task_list if task.task_id != task_id]

    def view_tasks_by_status(self, status):
        """
        Returns a list of tasks filtered by status.
        """
        return [task for task in self.task_list if task.status.lower() == status.lower()]
