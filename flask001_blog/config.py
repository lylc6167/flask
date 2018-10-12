# from oslo_config import


class Config(object):
    SECRET_KEY = 'XpG/bck8hgX9o4AJh87dLw=='  # python随机生成


class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass
    # Open the DEBUG
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/flask001_blog'
