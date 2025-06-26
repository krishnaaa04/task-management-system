from flask import Flask, request, jsonify, render_template
from manager.task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

# Serve the frontend page
@app.route('/')
def home():
    return render_template("index.html")

# Create a new user (auto user_id)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    name = data['name']
    email = data['email']
    task_manager.create_user(name, email)
    return jsonify({"message": "User created"}), 201

# Create a new task (auto task_id)
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    title = data['title']
    description = data.get('description', '')
    due_date = data.get('due_date', None)
    priority = data.get('priority', 'Medium')
    status = data.get('status', 'To Do')
    assigned_to = data.get('assigned_to', None)

    task_manager.create_task(title, description, due_date, priority, status, assigned_to)
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

# View all tasks
@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    tasks = task_manager.list_all_tasks()
    return jsonify([task.__dict__ for task in tasks]), 200

# View tasks assigned to a specific user
@app.route('/tasks/user/<int:user_id>', methods=['GET'])
def tasks_by_user(user_id):
    tasks = task_manager.list_tasks_by_user(user_id)
    return jsonify([task.__dict__ for task in tasks]), 200

# View tasks by their status
@app.route('/tasks/status/<status>', methods=['GET'])
def tasks_by_status(status):
    status = status.strip().title()
    tasks = task_manager.list_tasks_by_status(status)
    return jsonify([task.__dict__ for task in tasks]), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
