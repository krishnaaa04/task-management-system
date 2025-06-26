from flask import Flask, request, jsonify
from manager.task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

# Home route
@app.route('/')
def home():
    return "🎯 Task Management API is running!"

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = data['user_id']
    name = data['name']
    email = data['email']
    task_manager.create_user(user_id, name, email)
    return jsonify({"message": "User created"}), 201

# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = data['task_id']
    title = data['title']
    description = data['description']
    due_date = data['due_date']
    priority = data['priority']
    task_manager.create_task(task_id, title, description, due_date, priority)
    return jsonify({"message": "Task created"}), 201

# Assign a task to a user
@app.route('/tasks/<int:task_id>/assign/<int:user_id>', methods=['PUT'])
def assign_task(task_id, user_id):
    task_manager.assign_task_to_user(task_id, user_id)
    return jsonify({"message": "Task assigned"}), 200

# Update task status
@app.route('/tasks/<int:task_id>/status', methods=['PUT'])
def update_status(task_id):
    data = request.json
    new_status = data['status']
    task_manager.update_task_status(task_id, new_status)
    return jsonify({"message": "Status updated"}), 200

# Update task priority
@app.route('/tasks/<int:task_id>/priority', methods=['PUT'])
def update_priority(task_id):
    data = request.json
    new_priority = data['priority']
    task_manager.update_task_priority(task_id, new_priority)
    return jsonify({"message": "Priority updated"}), 200

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return jsonify({"message": "Task deleted"}), 200

# Get all tasks
@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    tasks = task_manager.list_all_tasks()
    return jsonify([task.__dict__ for task in tasks]), 200

# Get tasks by user
@app.route('/tasks/user/<int:user_id>', methods=['GET'])
def tasks_by_user(user_id):
    tasks = task_manager.list_tasks_by_user(user_id)
    return jsonify([task.__dict__ for task in tasks]), 200

# Get tasks by status
@app.route('/tasks/status/<status>', methods=['GET'])
def tasks_by_status(status):
    tasks = task_manager.list_tasks_by_status(status)
    return jsonify([task.__dict__ for task in tasks]), 200

if __name__ == '__main__':
    app.run(debug=True)
