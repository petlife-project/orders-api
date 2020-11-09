from flask_restful import Resource

from orders.api.services.polling import PollingService


class Shop(Resource):
    """ For a shop to accept/reject orders and get their current status."""

    @staticmethod
    def get():
        service = PollingService()
        return service.get_orders('petshop')

    @staticmethod
    def put():
        pass
