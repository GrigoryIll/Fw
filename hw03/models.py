from flask_sqlalchemy import SQLAlchemy
from wtforms import PasswordField
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), primary_key=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = generate_password_hash(password)   


    def __repr__(self):
        return f'User({self.surname} {self.name} {self.email})'