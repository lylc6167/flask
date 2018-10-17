from flask import Flask, redirect, url_for

from .models import db
from .controllers import blog, main
from .extensions import bcrypt


def create_app(object_name):

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(main.main_blueprint)

    return app