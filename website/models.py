from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
# from datetime import datetime
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship("Note")
# class List(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)   
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.now)
#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"