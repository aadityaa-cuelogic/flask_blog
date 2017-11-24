from flask import Blueprint, request, url_for, render_template, redirect, flash, session
from flask_login import current_user, login_required
from app import db
from .models import Post
from .forms import BlogForm

blog_module = Blueprint('blog', __name__)

@blog_module.route('/')
def index():
	posts = Post.query.order_by(Post.pub_date.desc()).all()
	return render_template('home.html', posts=posts)


@blog_module.route("/addblog", methods=['GET', 'POST'])
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

@blog_module.route('/deleteblog/<int:blog_id>')
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


@blog_module.route('/updateblog/<int:blog_id>', methods=['GET', 'POST'])
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
