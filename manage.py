# from flask.ext.script import Manager, Server
# 上述代码为https://blog.csdn.net/jmilk/article/details/53152158
# 文章中所填代码，和实际误差有点大
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

import main
import models


manager = Manager(main.app)
migrate = Migrate(main.app, models.db)

manager.add_command("server", Server())
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=main.app,
        db=models.db,
        User=models.User,
        Post=models.Post,
        Comment=models.Comment)


if __name__ == '__main__':
    manager.run()
