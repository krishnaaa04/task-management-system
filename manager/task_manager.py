from models.task import Task
from models.user import User
from db.db_config import get_connection

class TaskManager:
    def create_user(self, user_id, name, email):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (user_id, name, email) VALUES (%s, %s, %s)", (user_id, name, email))
            conn.commit()
            print("User created.")
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def create_task(self, task_id, title, description, due_date, priority):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tasks (task_id, title, description, due_date, priority)
                VALUES (%s, %s, %s, %s, %s)
            """, (task_id, title, description, due_date, priority))
            conn.commit()
            print("Task created.")
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def assign_task_to_user(self, task_id, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET assigned_to = %s WHERE task_id = %s", (user_id, task_id))
            conn.commit()
            print("Task assigned.")
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_task_status(self, task_id, new_status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET status = %s WHERE task_id = %s", (new_status, task_id))
            conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def update_task_priority(self, task_id, new_priority):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE tasks SET priority = %s WHERE task_id = %s", (new_priority, task_id))
            conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def delete_task(self, task_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
            conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()
            conn.close()

    def list_all_tasks(self):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tasks")
            results = cursor.fetchall()
            return [Task(**row) for row in results]
        except Exception as e:
            print("Error:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def list_tasks_by_user(self, user_id):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tasks WHERE assigned_to = %s", (user_id,))
            results = cursor.fetchall()
            return [Task(**row) for row in results]
        except Exception as e:
            print("Error:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def list_tasks_by_status(self, status):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tasks WHERE status = %s", (status,))
            results = cursor.fetchall()
            return [Task(**row) for row in results]
        except Exception as e:
            print("Error:", e)
            return []
        finally:
            cursor.close()
            conn.close()

    def get_task(self, task_id):
        try:
            conn = get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
            result = cursor.fetchone()
            if result:
                return Task(**result)
            return None
        except Exception as e:
            print("Error:", e)
            return None
        finally:
            cursor.close()
            conn.close()
