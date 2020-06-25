from flask import request, make_response
from app.models import Order
from app.schemas import OrderSchema
from app.enums import OrderStatus
from app import db
from flask import jsonify
from datetime import datetime

HEADERS = {'Content-Type': 'application/json'}

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class OrdersController:
    def index(self):
        orders = Order.query.all()
        return make_response(jsonify(orders_schema.dump(orders)), 200, HEADERS)

    def show(self, id):
        order = Order.query.get_or_404(id)
        return make_response(jsonify(order_schema.dump(order)), 200, HEADERS)

    def create(self):
        user_id = request.get_json().get('user_id')
        created_at = datetime.now()
        status = OrderStatus.PENDING
        value = request.get_json().get('value')

        order = Order(user_id, created_at, status, value)
        db.session.add(order)
        db.session.commit()

        return make_response(jsonify(order_schema.dump(order)), 201, HEADERS)

    def delete(self, id):
        order = Order.query.get_or_404(id)
        db.session.delete(order)
        db.session.commit()

        return make_response(jsonify(order_schema.dump(order)), 200)

    def update(self, id):
        update_params = request.get_json()

        order = Order.query.filter_by(id=id)

        order.update(update_params)
        db.session.commit()

        order = Order.query.get_or_404(id)

        return make_response(order_schema.dump(order), 200, HEADERS)

