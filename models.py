from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.Text())
    tasks = db.relationship("Tasks", backref="user")

    #password_hash = db.Column(db.String(120))
    #joined = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

    def __repr__(self):
        return f"User:{self.username}, email:{self.email}"
    
    def generate_password(self, password):
        self.password = generate_password_hash(password) 
    
    def check_password(self, password):
        return check_password_hash(self.password,password)
    
    @classmethod
    def get_user_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_email(cls, email):
        return cls.query.filter_by(email=email).first()


    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()





class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    to_do = db.Column(db.String(30), unique=False)
    priority = db.Column(db.String(10), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    
    def __repr__(self):
        return f"You need to {self.to_do}"
    

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def save(self):
        db.session.add(self)
        db.session.commit()


