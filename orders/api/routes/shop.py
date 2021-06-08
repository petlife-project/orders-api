from flask_restful import Resource
from flask_jwt_extended import jwt_required

from orders.api.services.polling import get_orders
from orders.api.services.change_status import ChangeStatusService


class Shop(Resource):
    """ For a shop to accept/reject orders and get their current status."""

    @staticmethod
    @jwt_required
    def get():
        return get_orders()

    @staticmethod
    @jwt_required
    def put():
        service = ChangeStatusService()
        return service.confirm()

    @staticmethod
    @jwt_required
    def delete():
        service = ChangeStatusService()
        return service.reject()
