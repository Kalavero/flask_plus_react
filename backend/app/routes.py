from flask import current_app as app
from controllers import users_controller

@app_route('/', methods=['GET'])
def users_index():
    UsersController().index()
