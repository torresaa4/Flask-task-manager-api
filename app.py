from flask import Flask, jsonify
from extensions import db, jwt
from auth import auth_bp
from tasks import tasks_bp
from user import user_bp






def create_app():
    app = Flask(__name__)

    app.config.from_prefixed_env()


    ##init exts
    db.init_app(app)
    jwt.init_app(app)


    #register blueprints
    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(tasks_bp, url_prefix='/tasks')
    app.register_blueprint(user_bp, url_prefix='/user')

    # jwt error handlers
    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_data):
        return jsonify({"message": "Token has expired", "error": "token_expired"}), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        print("JWT ERROR:", error)
        return jsonify({
        "message": "Signature verification failed",
        "error": "invalid_token"
        }), 401

    @jwt.unauthorized_loader
    def missing_token(error):
        return jsonify({"message": "request does not contain valid token", "error": "authorization_header"}), 401


    return app










    

