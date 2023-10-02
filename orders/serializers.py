from .models import Order
from django.forms import model_to_dict


class OrderSerializer:
    def __init__(self, order):
        self.order = order

    def data(self):
        return model_to_dict(self.order)
