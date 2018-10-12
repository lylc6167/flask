from flask import Flask, redirect, url_for

from .models import db
from .controllers import blog


def create_app(object_name):

