from orders.utils.db.adapter_factory import get_mongo_adapter
from orders.api.body_parsers.order_placement import parse_req


def place_order():
    """ Calls the methods that transform the fields
        and creates the control fields, inserting in MongoDB afterwards

        Args:
            All the fields from the request parser.

        Returns:
            200 status if everything works.
    """
    doc = parse_req()
    _resolve_request_fields(doc)
    doc['status'] = {
        'confirmed': False,
        'cancelled': False,
        'rejected': False
    }
    mongo = get_mongo_adapter()
    mongo.place_order(doc)
    return 200


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
