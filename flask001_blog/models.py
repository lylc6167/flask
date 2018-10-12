from flask_sqlalchemy import SQLAlchemy
# from flask001_blog.__init__ import app # 初始化后不需要了
# from sqlalchemy import *  # 此方法可以省略部分代码，尚未测试


db = SQLAlchemy()  # 在pycharm2017中可以正常使用，并且db.Column可以正常提示

# a=Column(String(45),)


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return "<Model User '{}'>".format(self.username)


posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))


class Post(db.Model):

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(355))
    text = db.Column(db.Text())
    created_date = db.Column(db.DateTime)

    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))

    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')

    tags = db.relationship(
        'Tag',
        secondary='posts_tags',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):  # 命令行修改语句
        return "<Model Post '{}'>".format(self.title)


class Comment(db.Model):

    __tabelname__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    created_time = db.Column(db.DateTime())

    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Comment '{}'>".format(self.name)


class Tag(db.Model):

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag '{}'>".format(self.name)