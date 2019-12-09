from flask import Blueprint
from flask import current_app

from distoreapp.database import session
from distoreapp.models import *

bp = Blueprint("static", __name__)

