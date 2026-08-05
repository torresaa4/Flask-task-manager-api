from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import UserModel
from schemas import UserSchema
from extensions import db

user_bp = Blueprint('user', __name__)



@user_bp.get('/all_users')
def get_users():

    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=3, type=int)

    users = UserModel.query.paginate(
        page = page,
        per_page = per_page
    )

    results = UserSchema().dump(users.items, many=True)

    return jsonify({"Users": results}), 200



@user_bp.patch('/<int:user_id>')
@jwt_required()
def update_user(user_id):
    current_user = int(get_jwt_identity())
    data = request.get_json()
    user = UserModel.query.filter_by(id=user_id).first()

    if user is None:
        return jsonify({"message": "user not found"}), 404

    if user.id != current_user:
        return jsonify({"message": "cant update other users"}), 403
        
    if "username" in data:
        if not data["username"].strip():
            return jsonify({"error": "username cant be empty"}), 400

        existing_user = UserModel.get_user_username(data["username"])

        if existing_user and existing_user.id != current_user:
            return jsonify({"error": "Username already exists"}), 409
        
        user.username = data["username"]

    if "email" in data:
        if not data["email"].strip():
            return jsonify({"error": "email cant be empty"}), 400

        existing_email = UserModel.get_email(data["email"])

        if existing_email and existing_email.id != current_user:
            return jsonify({"error": "Email already exists"}), 409
        
        user.email = data["email"]
    
    if "password" in data:
        if not data["password"]:
            return jsonify({"error": " password cant be empty"}), 400
        user.generate_password(password=data["password"])
    db.session.commit()
    
    return jsonify({"message": "user updated"}), 200





@user_bp.delete('/<int:user_id>')
@jwt_required()
def delete_user(user_id):
    current_user = int(get_jwt_identity())

    user = UserModel.query.filter_by(id=user_id).first()

    if user.id != current_user:
        return jsonify({"message": "cant delete other users"}), 403
    
    user.delete()
    db.session.commit()
    return jsonify({"message": "user deleted"}), 200