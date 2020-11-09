from flask_restful import Resource

from orders.api.services.order_placement import OrderPlacementService


class Client(Resource):
    """ For a client to place/cancel orders and get their current status."""

    @staticmethod
    def get():
        pass

    @staticmethod
    def post():
        service = OrderPlacementService()
        return service.place_order()

    @staticmethod
    def put():
        pass
