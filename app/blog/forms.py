"""
Form module for required validation.
"""
import flask_wtf
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from .models import db, User
from wtforms.validators import DataRequired, Email, Length, EqualTo

class BlogForm(Form):
    """
    Add a blog
    """
    
    title = StringField('Title',validators=[DataRequired()])
    description =TextAreaField('Description',validators=[DataRequired()])
    post = SubmitField('Post')