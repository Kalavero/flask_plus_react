from flask import request
from app.models import User
from app.schemas import UserSchema
from app import db
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
        db.session.add(user)
        db.session.commit()

        return jsonify(user_schema.dump(user))

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()

        return jsonify(user_schema.dump(user)), 200

