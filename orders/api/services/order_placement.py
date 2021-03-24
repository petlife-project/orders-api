from orders.utils.db.adapter_factory import get_mongo_adapter
from orders.api.body_parsers.order_placement import OrderPlacementParser


class OrderPlacementService:
    """ This service places an order for a petshop, with an initial state
        waiting for confirmation/rejection or a cancellation.
    """
    def __init__(self):
        self.parser = OrderPlacementParser()

    def place_order(self):
        """ Calls the methods that transform the fields
            and creates the control fields, inserting in MongoDB afterwards

            Args:
                All the fields from the request parser.

            Returns:
                200 status if everything works.
        """
        doc = self.parser.fields
        self._resolve_request_fields(doc)
        self._create_control_fields(doc)
        self._insert_in_mongo(doc)
        return 200

    @staticmethod
    def _resolve_request_fields(doc):
        doc['petshop'] = {
            'username': doc['petshop_username'],
            'name': doc['petshop_name']
        }
        del doc['petshop_username']
        del doc['petshop_name']

        doc['service'] = {
            'id': doc['service_id'],
            'name': doc['service_name']
        }
        del doc['service_id']
        del doc['service_name']

        doc['client'] = {
            'username': doc['client_username'],
            'name': doc['client_name'],
            'pet': (doc['client_pet'])
        }
        del doc['client_username']
        del doc['client_name']
        del doc['client_pet']

        doc['schedule'] = {
            'datetime': doc['schedule_datetime']
        }
        del doc['schedule_datetime']

    @staticmethod
    def _create_control_fields(doc):
        doc['status'] = {
            'confirmed': False,
            'cancelled': False,
            'rejected': False
        }

    @staticmethod
    def _insert_in_mongo(doc):
        mongo = get_mongo_adapter()
        mongo.place_order(doc)
