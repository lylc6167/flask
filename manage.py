# from flask.ext.script import Manager, Server
# 上述代码为https://blog.csdn.net/jmilk/article/details/53152158
# 文章中所填代码，和实际误差有点大
from flask import Flask, redirect, url_for
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from flask001_blog import models
from flask001_blog.config import DevConfig
from flask001_blog.models import db
from flask001_blog.controllers.blog import blog_blueprint


app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

manager = Manager(app)
migrate = Migrate(app, models.db)
manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=models.db,
        User=models.User,
        Post=models.Post,
        Comment=models.Comment,
        Tag=models.Tag)


@app.route('/')
def index():
    return redirect(url_for('blog.home'))

app.register_blueprint(blog_blueprint)

if __name__ == '__main__':
    manager.run()
    app.run()
