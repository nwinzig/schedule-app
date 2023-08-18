from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# employee table
class Employee(db.Model, UserMixin):
    __tablename__ = 'employees'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable = False)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    # relationship
    office_id = db.Column(db.Integer, db.ForeignKey
    (add_prefix_for_prod('offices.id')), nullable=False)
    shifts = db.relationship('Shift', backref='employee', lazy=True)


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email
        }

# office table
class Office(db.Model):
    __tablename__ = 'offices'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    # relationship
    employees = db.relationship('Employee', backref='office', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'employees': self.employees
        }

# shift table
class Shift(db.Model):
    __tablename__ = 'shifts'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    hours = db.Column(db.Integer, nullable=False)

    # relationship
    employee_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('employees.id')), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date,
            'hours': self.hours,
            'employee_id': self.employee_id
        }
