from app.models import db, Employee, environment, SCHEMA, Shift, Office
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_employees():
    demo = Employee(
        name='Jack Johnson', username='jjohnson', email='demo@aa.io', password='password')
    demo2 = Employee(
        name="Marnie O'Hare",username="mO'Hare", email='marnie@aa.io', password='password')
    demo3 = Employee(
        name="Bobby Brown", username='bBrown', email='bobbie@aa.io', password='password')

    db.session.add(demo)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.commit()


def undo_employees():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM employees"))

    db.session.commit()
