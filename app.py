from flask import Flask, request, jsonify
from manager.task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def home():
    return "🎯 Task Management API is running!"

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    try:
        user_id = int(data['user_id'])
        name = data['name'].strip()
        email = data['email'].strip()
        task_manager.create_user(user_id, name, email)
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    try:
        task_id = int(data['task_id'])
        title = data['title'].strip()
        description = data['description'].strip()
        due_date = data['due_date'].strip()
        priority = data['priority'].strip().capitalize()
        if priority not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid priority.")
        task_manager.create_task(task_id, title, description, due_date, priority)
        return jsonify({"message": "Task created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/<int:task_id>/assign/<int:user_id>', methods=['PUT'])
def assign_task(task_id, user_id):
    try:
        task_manager.assign_task_to_user(task_id, user_id)
        return jsonify({"message": "Task assigned"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/<int:task_id>/status', methods=['PUT'])
def update_status(task_id):
    data = request.json
    try:
        new_status = data['status'].strip().title()
        if new_status not in ["To Do", "In Progress", "Done"]:
            raise ValueError("Invalid status.")
        task_manager.update_task_status(task_id, new_status)
        return jsonify({"message": "Status updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/<int:task_id>/priority', methods=['PUT'])
def update_priority(task_id):
    data = request.json
    try:
        new_priority = data['priority'].strip().capitalize()
        if new_priority not in ["Low", "Medium", "High"]:
            raise ValueError("Invalid priority.")
        task_manager.update_task_priority(task_id, new_priority)
        return jsonify({"message": "Priority updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    try:
        task_manager.delete_task(task_id)
        return jsonify({"message": "Task deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks', methods=['GET'])
def list_all_tasks():
    try:
        tasks = task_manager.list_all_tasks()
        return jsonify([task.__dict__ for task in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/user/<int:user_id>', methods=['GET'])
def tasks_by_user(user_id):
    try:
        tasks = task_manager.list_tasks_by_user(user_id)
        return jsonify([task.__dict__ for task in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/tasks/status/<status>', methods=['GET'])
def tasks_by_status(status):
    try:
        status = status.strip().title()
        if status not in ["To Do", "In Progress", "Done"]:
            raise ValueError("Invalid status.")
        tasks = task_manager.list_tasks_by_status(status)
        return jsonify([task.__dict__ for task in tasks]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
