import datetime
from app import db
from app.user.models import User

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text)
	pub_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	pub_date = db.Column(db.DateTime, default=datetime.datetime.now)