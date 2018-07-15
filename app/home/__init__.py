# app/admin/__init__.py

from flask import Blueprint

bp = Blueprint('home', __name__)

from . import routes
