# from flask.ext.script import Manager, Server
# 上述代码为https://blog.csdn.net/jmilk/article/details/53152158
# 文章中所填代码，和实际误差有点大
import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from flask001_blog import models
from flask001_blog import create_app


env = os.environ.get('flask001_blog', 'dev')  # 与18节微妙差别
app = create_app('flask001_blog.config.%sConfig' % env.capitalize())
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
        Tag=models.Tag,
        Server = Server)


if __name__ == '__main__':
    manager.run()
