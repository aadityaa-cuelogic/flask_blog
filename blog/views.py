from flask import Blueprint, request, url_for, render_template, redirect, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from . import app, db
from .models import User, Post
from .forms import SignupForm, SigninForm, BlogForm


@app.route('/')
def index():
	posts = Post.query.order_by(Post.pub_date.desc()).all()
	return render_template('home.html', posts=posts)

@app.route("/adduser", methods=['GET', 'POST'])
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

@app.route("/login", methods=['GET', 'POST'])
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

@app.route("/logout")
@login_required
def logoutUser():
	logout_user()
	flash("Logged Out")
	return redirect(url_for('index'))


@app.route("/addblog", methods=['GET', 'POST'])
@login_required
def addblog():
	form = BlogForm(request.form)

	if form.validate_on_submit():
		post = Post(
					title=form.title.data,
					description=form.description.data,
					pub_by=current_user.id
				)
		db.session.add(post)
		db.session.commit()
		flash('Post added successfully')
		return redirect(url_for('index'))
	return render_template('addblog.html', form=form)

@app.route('/deleteblog/<int:blog_id>')
@login_required
def deleteblog(blog_id):
	try:
		post = Post.query.filter_by(id=blog_id).first()
	except:
		return redirect(url_for('index'))

	if post is not None:
		db.session.delete(post)
		db.session.commit()
		flash("Post deleted")
	return redirect(url_for('index'))


@app.route('/updateblog/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def updateblog(blog_id):
	form = BlogForm()
	try:
		post = Post.query.filter_by(id=blog_id).first()
	except:
		return redirect(url_for('index'))

	if post is not None and form.validate_on_submit():
		post.title = form.title.data
		post.description = form.description.data
		db.session.commit()
		flash("Post Updated")
	else:
		form.title.data = post.title
		form.description.data = post.description
		return render_template('addblog.html', form=form)
	return redirect(url_for('index'))
