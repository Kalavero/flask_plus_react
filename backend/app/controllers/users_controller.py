from flask import request, make_response
from app.models import User
from app import db
from app.schemas import UserSchema
from flask import jsonify

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class UsersController:
    def index(self):
        users = User.query.all()
        return jsonify(users_schema.dump(users))

    def create(self):
        first_name = request.args.get('first_name')
        last_name = request.args.get('last_name')
        email = request.args.get('email')

        user = User(first_name, last_name, email)
        user.save

        return jsonify(user_schema.dump(user))
