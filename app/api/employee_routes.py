from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Employee, Shift, Office

employee_routes = Blueprint('employee', __name__)


@employee_routes.route('/')
@login_required
def employees():
    """
    Query for all employees and returns them in a list of employees dictionaries
    """
    employees = Employee.query.all()
    return {'employees': [employee.to_dict() for employee in employees]}


@employee_routes.route('/<int:id>')
@login_required
def employee(id):
    """
    Query for a employee by id and returns that employee in a dictionary
    """
    employee = Employee.query.get(id)
    return employee.to_dict()
