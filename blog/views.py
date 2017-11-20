from flask import Blueprint, request, url_for, render_template, redirect
from . import app, db
from .models import User, Post
from .forms import SignupForm, SigninForm


@app.route('/')
def index():
	return "Hello World"

@app.route("/adduser", methods=['GET', 'POST'])
def addUser():
	form = SignupForm(request.form)
	# if form.validate_on_submit():
	if request.method == 'POST':
		user = User(name=form.name.data, username=form.username.data, 
					email=form.email.data, password=form.password.data
			   )
		db.session.add(user)
		db.session.commit()
		return "User added successfully"
	return "Hello Get AddUser"