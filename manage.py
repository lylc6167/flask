# from flask.ext.script import Manager, Server
# 上述代码为https://blog.csdn.net/jmilk/article/details/53152158
# 文章中所填代码，和实际误差有点大
from flask_script import Manager, Server
import main
import models


manager = Manager(main.app)

manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(
        app=main.app,
        db=models.db,
        User=models.User,
        Post=models.Post)


if __name__ == '__main__':
    manager.run()
