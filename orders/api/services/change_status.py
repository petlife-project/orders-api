from flask_restful import abort
from flask_jwt_extended import get_jwt_identity

from orders.api.body_parsers.change_status import parse_req
from orders.utils.db.adapter_factory import get_mongo_adapter


# pylint: disable=inconsistent-return-statements
class ChangeStatusService:
    """ Class for sharing some logic between similar actions
        Confirm, reject or cancel order

        Returning 200 or 404
    """
    def __init__(self):
        self.order_id = parse_req()
        self.user = get_jwt_identity()
        self.mongo = get_mongo_adapter()

    def confirm(self):
        try:
            self.mongo.confirm_order(self.order_id, self.user)
            return 200
        except KeyError as error:
            abort(404, extra=f'{error}')

    def reject(self):
        try:
            self.mongo.reject_order(self.order_id, self.user)
            return 200
        except KeyError as error:
            abort(404, extra=f'{error}')

    def cancel(self):
        try:
            self.mongo.cancel_order(self.order_id, self.user)
            return 200
        except KeyError as error:
            abort(404, extra=f'{error}')
