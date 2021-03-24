from flask_restful import abort

from orders.api.body_parsers.change_status import ChangeStatusParser
from orders.utils.db.adapter_factory import get_mongo_adapter


class CancellationService:
    """ Service responsible for changing an order status to cancelled
        using order_id provided by the user.
    """
    def __init__(self):
        self.parser = ChangeStatusParser()

    def cancel(self):
        """ Gets argument and calls update method, returning a standard 200 response.
            If a problem occurs when updating, the process is aborted right away.
        """
        order_id = self.parser.field
        self._update_in_mongo(order_id)
        return 200

    @staticmethod
    def _update_in_mongo(order_id):
        mongo = get_mongo_adapter()
        try:
            mongo.cancel_order(order_id)
        except KeyError as error:
            abort(404, extra=f'{error}')
