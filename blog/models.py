import datetime
from . import app, db, login_manager
from flask_login import UserMixin

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(120), nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False, index=True)
	password = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(80), unique=True, nullable=False)
	post = db.relationship('Post', backref='user',cascade="all,delete",lazy='dynamic')

	def verify_password(self, password):
		if self.password == password:
			return True
		return False

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.Text, nullable=False)
	description = db.Column(db.Text)
	pub_by = db.Column(db.Integer, db.ForeignKey('user.id'))
	pub_date = db.Column(db.DateTime, default=datetime.datetime.now)

@login_manager.user_loader
def load_user(ident):
	return User.query.get(int(ident))