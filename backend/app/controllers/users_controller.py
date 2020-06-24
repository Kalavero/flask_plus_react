from flask import request, make_response
from flask import current_app as app
from models.user import db, user

class UsersController:
    def index():
        return 'all users'

