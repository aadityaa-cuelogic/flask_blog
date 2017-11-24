from . import app
from .blog.views import blog_module
from .user.views import user_module

app.register_blueprint(blog_module)
app.register_blueprint(user_module)
