import os
SECRET_KEY="MY_SECRET_KEY"
SQLALCHEMY_DATABASE_URI= os.environ['DATABASE_URL']
# export DATABASE_URL="postgres://postgres:root@localhost:5432/blog_app
SQLALCHEMY_TRACK_MODIFICATIONS=False