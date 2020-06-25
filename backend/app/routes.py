from flask import current_app as app
from app.controllers import UsersController
from app.controllers import OrdersController

@app.route('/clientes', methods=['GET'])
@app.route('/users', methods=['GET'])
def users_index():
    return UsersController().index()

@app.route('/clientes/<id>', methods=['GET'])
@app.route('/users/<id>', methods=['GET'])
def users_show(id):
    return UsersController().show(id)

@app.route('/clientes', methods=['POST'])
@app.route('/users', methods=['POST'])
def users_create():
    return UsersController().create()

@app.route('/clientes/<id>', methods=['DELETE'])
@app.route('/users/<id>', methods=['DELETE'])
def users_delete(id):
    return UsersController().delete(id)

@app.route('/clientes/<id>', methods=['PUT'])
@app.route('/users/<id>', methods=['PUT'])
def users_update(id):
    return UsersController().update(id)

@app.route('/pedidos', methods=['GET'])
@app.route('/orders', methods=['GET'])
def orders_index():
    return OrdersController().index()

@app.route('/pedidos/<id>', methods=['GET'])
@app.route('/orders/<id>', methods=['GET'])
def orders_show(id):
    return OrdersController().show(id)

@app.route('/pedidos', methods=['POST'])
@app.route('/orders', methods=['POST'])
def orders_create():
    return OrdersController().create()

@app.route('/pedidos/<id>', methods=['DELETE'])
@app.route('/orders/<id>', methods=['DELETE'])
def orders_delete(id):
    return OrdersController().delete(id)

@app.route('/pedidos/<id>', methods=['PUT'])
@app.route('/orders/<id>', methods=['PUT'])
def orders_update(id):
    return OrdersController().update(id)
