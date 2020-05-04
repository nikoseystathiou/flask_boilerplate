from application.models import db
from flask_security import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid

class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))

# Define models for the users and user roles
class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirm = db.Column(db.DateTime())
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean())
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Role', secondary='user_roles', backref='User', lazy=True)

    def __str__(self):
        return self.username