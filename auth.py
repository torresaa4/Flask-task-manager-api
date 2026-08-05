from flask import Blueprint,jsonify, request, current_app
from models import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.post('/register')
def register_user():

    data = request.get_json()

    # username check
    if not data.get("username"):
        return jsonify({"error": "username is required"}), 400

    user = UserModel.get_user_username(username=data.get('username'))

    # if user already exits
    if user is not None:
        return jsonify({"error": "username already exists"}), 409

    # email check
    if not data.get("email"):
        return jsonify({"error": "email is required"}), 400

    email = UserModel.get_email(email=data.get('email'))

    if email is not None:
        return jsonify({"error": "email already exists"}), 409


    # call generate_password function in models.py to hash password and verify its not empty
    if not data.get("password"):
        return jsonify({"error": "password is required"}), 400

    

    new_user = UserModel(
            username = data.get('username'),
            email = data.get('email'))

    
    new_user.generate_password(password=data.get('password'))
    # call save function
    new_user.save()
    
    return jsonify({"message": "User created"}), 201



@auth_bp.post('/login')
def login_user():
    data = request.get_json()
    # username and password check
    if not data.get("username"):
        return jsonify({"error": "username is required"}), 400

    if not data.get("password"):
        return jsonify({"error": "password is required"}), 400
    
    # call get_user_username fucntion to get username
    user = UserModel.get_user_username(username=data.get('username'))
    
    # if user exist and password provided matches password in database
    # call check_password function to check hashed passowrd
    if user and (user.check_password(password=data.get('password'))):

        # create access and refresh tokens for user per login
        access_token = create_access_token(identity=str(user.id))
        refresh_token = create_refresh_token(identity=str(user.id))

        


        return jsonify(
            {"message": "Logged in",
             "tokens": {
                 "access": access_token,
                 "refresh": refresh_token
                }
            }
        ), 200
    return jsonify({"error": "Invalid username or password"}), 401


@auth_bp.post('/refresh')
@jwt_required(refresh=True)
def refresh_access():
    current_user = int(get_jwt_identity())

    new_token = create_access_token(identity=str(current_user))


    return jsonify({"access token": new_token}), 200