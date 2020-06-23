class OrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'status', 'value')
        include_fk = True

