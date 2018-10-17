# from oslo_config import


class Config(object):
    SECRET_KEY = 'XpG/bck8hgX9o4AJh87dLw=='  # python随机生成
    # 一下仅用于reCAPTCHA账户验证
    # RECAPTCHA_PUBLIC_KEY = "<your public key>"
    # RECAPTCHA_PRIVATE_KEY = "<your private key>"

class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass
    # Open the DEBUG
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/flask001_blog'
