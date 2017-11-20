import datetime
from . import app, db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(120), nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False, index=True)
	password = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text)
	pub_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	pub_date = db.Column(db.DateTime, default=datetime.datetime.now)