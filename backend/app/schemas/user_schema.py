class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

