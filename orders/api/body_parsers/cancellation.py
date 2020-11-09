from flask_restful.reqparse import RequestParser


class CancellationParser:
    """ Parser for the cancellation service, where an order id
        is provided to change its status to cancelled.
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
