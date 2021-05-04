import re

from flask_restful import abort
from flask.json import jsonify

from orders.api.body_parsers.polling import PollingParser
from orders.utils.db.adapter_factory import get_mongo_adapter


# pylint: disable=inconsistent-return-statements
class PollingService:
    """ Service responsible for getting all the orders related to an user
        The user is identified through the username sent on the request
        and the type (petshop or client) through the route used.

        Returns:
            List of orders related to that username
    """
    def __init__(self):
        self.parser = PollingParser()

    def get_orders(self, type_):
        """ Gets the sender's username, validates the input
            and returns the search results list
        """
        username = self.parser.field
        self._check_forbidden_characters(username)

        field = f'{type_}.username'
        query = {field: username}
        mongo = get_mongo_adapter()

        try:
            orders = mongo.search(query)
            return jsonify(orders)
        except KeyError as error:
            abort(404, extra=f'{error}')

    @staticmethod
    def _check_forbidden_characters(user_input):
        if re.match(r'{([^}]+)}', user_input):
            abort(403, extra='Invalid username')
