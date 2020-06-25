from flask import current_app as app
from app.controllers import UsersController
from app.controllers import OrdersController

@app.route('/users', methods=['GET'])
def users_index():
    return UsersController().index()

@app.route('/users/<id>', methods=['GET'])
def users_show(id):
    return UsersController().show(id)

@app.route('/users', methods=['POST'])
def users_create():
    return UsersController().create()

@app.route('/users/<id>', methods=['DELETE'])
def users_delete(id):
    return UsersController().delete(id)

@app.route('/users/<id>', methods=['PUT'])
def users_update(id):
    return UsersController().update(id)
