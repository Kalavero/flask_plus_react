import enum

class OrderStatus(str, enum.Enum):
    PENDING = 'pending'
    FINISHED = 'finished'

