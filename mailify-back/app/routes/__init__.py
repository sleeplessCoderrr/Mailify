from flask import Blueprint

email_bp = Blueprint('email', __name__)

from .email_routes import *
