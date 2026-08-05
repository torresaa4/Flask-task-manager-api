from app import create_app
from models import UserModel, Tasks
from extensions import db
from dotenv import load_dotenv
load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()
    print("Database created!")