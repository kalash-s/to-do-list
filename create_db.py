from app import app1, db

with app1.app_context():
    db.create_all()

from models import Task
from datetime import datetime
from app import db
t = Task(title="Shopping", date=datetime.utcnow())
db.session.add(t)