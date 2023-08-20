from app.models import db, Employee, environment, SCHEMA, Shift, Office
from sqlalchemy.sql import text
from datetime import date

# employee seeds
def seed_employees():
    demo = Employee(
        name='Jack Johnson', username='jjohnson', email='demo@aa.io', password='password', office_id=1)
    demo2 = Employee(
        name="Marnie O'Hare",username="mO'Hare", email='marnie@aa.io', password='password', office_id=2)
    demo3 = Employee(
        name="Bobby Brown", username='bBrown', email='bobbie@aa.io', password='password', office_id=2)

    db.session.add(demo)
    db.session.add(demo2)
    db.session.add(demo3)
    db.session.commit()


def undo_employees():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.employees RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM employees"))

    db.session.commit()


# office seeds
def seed_offices():
    office = Office(name='South Branch')
    office2 = Office(name='North Branch')
    office3 = Office(name='West Branch')
    office4 = Office(name= 'East Branch')

    db.session.add(office)
    db.session.add(office2)
    db.session.add(office3)
    db.session.commit()

def undo_offices():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.offices RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM offices"))

    db.session.commit()


# shift seeds
def seed_shifts():
    shift = Shift(date=date(2023,8,15), hours=8, employee_id=1)
    shift2 = Shift(date=date(2023,8,16), hours=6, employee_id=2)
    shift3 = Shift(date=date(2023,8,17), hours=7, employee_id=3)

    db.session.add(shift)
    db.session.add(shift2)
    db.session.add(shift3)
    db.session.commit()

def undo_shifts():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shifts RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shifts"))

    db.session.commit()
