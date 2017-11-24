from flask import Blueprint, request, url_for, render_template, redirect, flash, session
from flask_login import login_user, logout_user, login_required
from app import db
from .models import User
from .forms import SignupForm, SigninForm

user_module = Blueprint('user', __name__)

@user_module.route("/adduser", methods=['GET', 'POST'])
def addUser():
	form = SignupForm(request.form)
	
	if form.validate_on_submit():
		user = User(name=form.name.data, username=form.username.data, 
					email=form.email.data, password=form.password.data
			   )
		db.session.add(user)
		db.session.commit()
		flash("User added successfully")
		return redirect(url_for('index'))
	# print form.validate()
	# print form.errors
	return render_template('register.html', form=form)

@user_module.route("/login", methods=['GET', 'POST'])
def loginUser():
	form = SigninForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user)
			flash("Login Successful")
			return redirect(url_for('index'))
		flash("Login Failed")
	return render_template('login.html', form=form)

@user_module.route("/logout")
@login_required
def logoutUser():
	logout_user()
	flash("Logged Out")
	return redirect(url_for('index'))