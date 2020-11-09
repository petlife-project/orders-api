from flask_restful.reqparse import RequestParser


class ChangeStatusParser:
    """ Parser for the cancellation, confirmation and rejection services,
        where an order's id is provided and its status is set to one of
        the three based on the route and method used.
    """
    def __init__(self):
        parser = RequestParser()
        parser.add_argument(
            name='order_id',
            type=str,
            location='args',
            required=True
        )
        self.field = parser.parse_args()['order_id']
