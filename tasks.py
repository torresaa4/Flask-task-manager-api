from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Tasks, UserModel
from extensions import db
from schemas import TaskSchema

tasks_bp = Blueprint('task',__name__)


@tasks_bp.get('/my_tasks')
@jwt_required()
def user_tasks():
    current_user = int(get_jwt_identity())


    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=3, type=int)


    user = UserModel.query.get(current_user)

    if user is None:
        return jsonify({"error": "user not found"}), 404

    tasks = Tasks.query.filter_by(user_id=current_user).paginate(
        page = page,
        per_page= per_page)

    task_schema = TaskSchema()

    result = task_schema.dump(tasks.items, many=True)

    return jsonify({
        "username": user.username,
        "tasks": result }),200






@tasks_bp.post('/create')
@jwt_required()
def create_tasks():
    current_user = int(get_jwt_identity())

    data = request.get_json()

    priorities = ["low", "medium", "high"]

    # to do and priority check 
    if not data.get("to_do"):
        return jsonify({"error": "to do required"}), 400

    if not data.get("priority"):
        return jsonify({"error": "priority required"}), 400
    
    if data.get("priority").lower() not in priorities:
        return jsonify({"error": "priority must be low, medium or high"}), 400

    

    new_task = Tasks(
        to_do=data['to_do'],
        priority=data['priority'].lower(),
        user_id = current_user
    )
    new_task.save()

    return jsonify({"message": "Task has been created"}), 201


@tasks_bp.patch('/<int:task_id>')
@jwt_required()
def update_tasks(task_id):
    current_user = int(get_jwt_identity())
    data = request.get_json()
    task = Tasks.query.filter_by(id=task_id).first()
    priorities = ["low", "medium", "high"]

    if task is None:
        return jsonify({"message": "task not found"}), 404

    if task.user_id != current_user:
        return jsonify({"error": "user not authorizd to update this task"}), 403
    
    if "priority" in data:
        if data["priority"].lower() not in priorities:
            return jsonify({"error": "priority must be low, medium or high"}), 400
    
        task.priority = data["priority"].lower()

    if "to_do" in data:
        if not data["to_do"].strip():
            return jsonify({"error": "to do cant be empty"}), 400
        task.to_do = data["to_do"]

    db.session.commit()

    return jsonify({"message": "task updated"}), 200

@tasks_bp.delete('/<int:task_id>')
@jwt_required()
def delete_task(task_id):
    current_user = int(get_jwt_identity())
    
    task = Tasks.query.filter_by(id=task_id).first()

    if task is None:
        return jsonify({"message": "task not found"}), 404

    if task.user_id != current_user:
        return jsonify({"error": "user not authorizd to delete this task"}), 403
    
    task.delete()  
    db.session.commit() 
    
    return jsonify({"message": "task delted successfully"}), 200


