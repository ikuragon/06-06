from flask import Blueprint, render_template
from flask_login import login_required, current_user
# from sqlalchemy.orm import Session
#
from .db import db
# from app.models import Employee, Position, Division, Job
# from sqlalchemy.orm import sessionmaker
#
# bp = Blueprint('bp', __name__)
#
# @bp.route('/', methods=['GET'])
# def index():
#
# #    employees = Employee.join(Job, Employee.id == Job.employee_id).all()
#     job = Job.query.get(1)
#
#     employee_data = {
#         "second_name": "Voronova",
#         "first_name": "Daria",
#         "surname": "Dmitrievna",
#         "address": "c.Arkh s.Moskovskiy h.1 ",
#         "date_of_birth": "05.03.1982",
#
#         "employee_id": Employee.id
#
#     }
#
#     new_employee = Employee(**employee_data)
#
#     db.session.add(new_employee)
#     db.session.commit()
#
#     return '1'

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template(('index.html'))

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)