from flask import request, make_response
from app.models import User
from app.schemas import UserSchema
from app import db
from flask import jsonify

HEADERS = {'Content-Type': 'application/json'}

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UsersController:
    def index(self):
        users = User.query.all()
        return make_response(jsonify(users_schema.dump(users)), 200, HEADERS)

    def show(self, id):
        user = User.query.get_or_404(id)
        return make_response(jsonify(user_schema.dump(user)), 200, HEADERS)

    def create(self):
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        email = request.args.get('email')

        user = User(first_name, last_name, email)
        db.session.add(user)
        db.session.commit()

        return make_response(jsonify(user_schema.dump(user)), 201, HEADERS)

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()

        return make_response(jsonify(user_schema.dump(user)), 200)

    def update(self, id):
        update_params = {
                'first_name': request.args.get('first_name'),
                'last_name': request.args.get('last_name'),
                'email': request.args.get('email')
                }
        update_params = { k: v for k, v in update_params.items() if v is not None }

        user = User.query.filter_by(id=id)

        user.update(update_params)
        db.session.commit()

        user = User.query.get_or_404(id)

        return make_response(user_schema.dump(user), 200, HEADERS)

