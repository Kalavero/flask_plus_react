from app import db
from app.enums import OrderStatus

class Order(db.Model):
    __tablename_ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(OrderStatus), nullable=False)
    value = db.Column(db.Float)

    def __init__(self, user_id, created_at, status, value):
        self.user_id = user_id
        self.created_at = created_at
        self.status = status
        self.value = value

