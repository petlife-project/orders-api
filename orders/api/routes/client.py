from flask_restful import Resource
from flask_jwt_extended import jwt_required

from orders.api.services.order_placement import place_order
from orders.api.services.polling import get_orders
from orders.api.services.change_status import ChangeStatusService


class Client(Resource):
    """ For a client to place/cancel orders and get their current status."""

    @staticmethod
    @jwt_required
    def get():
        return get_orders()

    @staticmethod
    @jwt_required
    def post():
        return place_order()

    @staticmethod
    @jwt_required
    def delete():
        service = ChangeStatusService()
        return service.cancel()
