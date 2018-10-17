from flask_wtf import Form
from wtforms import (
    StringField,
    TextField,
    TextAreaField,
    PasswordField,
    BooleanField,
    ValidationError
)
from wtforms.validators import DataRequired, Length, EqualTo, URL

from .models import User


class LoginForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('此用户不存在，请重新输入用户名')
            return False

        if not user.check_password(self.password.data):
            self.username.errors.append('密码错误：请重新输入密码')
            return False

        return True


class RegisterForm(Form):
    username = StringField('Username', [DataRequired(), Length(max=255)])
    # 注意此处的min=8，由于没有提示信息导致测试时卡在这里没想明白,当密码小于8位页面不会跳转
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    password2 = PasswordField('Password_again', [DataRequired(),
                                                 EqualTo('password')])
    # recaptcha =

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('用户已存在')
            return False
        return True


class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])


class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )

    text = TextField(u'Comment', validators=[DataRequired()])