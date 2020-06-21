from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +os.path.join(basedir, '/config/db.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

# Init database
db = SQLAlchemy(app)

# Init marshmallow
marshmallow = Marshmallow(app)

# Run server
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0")
