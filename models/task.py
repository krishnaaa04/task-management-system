class Task:
    """
    Represents a task with attributes like title, description, due date, status, etc.
    """

    def __init__(self, task_id, title, description, due_date, priority, status="To Do", assigned_to=None):
        """
        Initializes a new Task instance.
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.assigned_to = assigned_to

    def update_status(self, new_status):
        """
        Updates the status of the task.
        """
        self.status = new_status

    def update_priority(self, new_priority):
        """
        Updates the priority of the task.
        """
        self.priority = new_priority

    def __str__(self):
        """
        Returns a formatted string representation of the task.
        """
        return (f"Task ID: {self.task_id}\n"
                f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Priority: {self.priority}\n"
                f"Status: {self.status}\n"
                f"Assigned To: {self.assigned_to or 'Unassigned'}")
