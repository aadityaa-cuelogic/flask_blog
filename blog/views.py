from flask import Blueprint, request, url_for, render_template, redirect, flash
from . import app, db
from .models import User, Post
from .forms import SignupForm, SigninForm


@app.route('/')
def index():
	return render_template('home.html')

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
		flash("User added successfully")
		return redirect(url_for('index'))
	return "Hello Get AddUser"