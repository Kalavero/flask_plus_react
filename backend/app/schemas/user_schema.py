from app import ma
from app.models import User

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

