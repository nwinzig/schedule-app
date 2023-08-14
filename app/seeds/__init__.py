from flask.cli import AppGroup
from .seeds import seed_employees, undo_employees, seed_offices, undo_offices, seed_shifts, undo_shifts

from app.models.db import db, environment, SCHEMA

seed_commands = AppGroup('seed')

# seed all
@seed_commands.command('all')
def seed():
    if environment == 'production':
        undo_shifts()
        undo_employees()
        undo_offices()
    seed_offices()
    seed_employees()
    seed_shifts()

# undo seeds
@seed_commands.command('undo')
def undo():
    undo_shifts()
    undo_employees()
    undo_offices()
