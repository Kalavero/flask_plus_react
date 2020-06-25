from flask import current_app as app
from app.controllers import UsersController
from app.controllers import OrdersController

@app.route('/users', methods=['GET'])
def users_index():
    return UsersController().index()

@app.route('/users', methods=['POST'])
def users_create():
    return UsersController().create()

@app.route('/users/<id>', methods=['DELETE'])
def users_delte(id):
    return UsersController().delete(id)
