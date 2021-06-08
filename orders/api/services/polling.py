from flask_restful import abort
from flask.json import jsonify
from flask_jwt_extended import get_jwt_identity

from orders.utils.db.adapter_factory import get_mongo_adapter


# pylint: disable=inconsistent-return-statements
def get_orders():
    """ Gets all orders from the requester

    Returns:
        200 - orders - (list<dict>)
        404 - If no orders
    """
    user = get_jwt_identity()
    username = user['username']
    type_ = user['type']

    field = f'{type_}.username'
    query = {field: username}
    mongo = get_mongo_adapter()

    try:
        orders = mongo.search(query)
        return jsonify(orders)
    except KeyError as error:
        abort(404, extra=f'{error}')
