from flask_restful.reqparse import RequestParser


def parse_req():
    """ Parser for the cancellation, confirmation and rejection services,
        where an order's id is provided and its status is set to one of
        the three based on the route and method used.

    Returns:
        order_id (str)
    """
    parser = RequestParser()
    parser.add_argument(
        name='order_id',
        type=str,
        location='args',
        required=True
    )
    return parser.parse_args()['order_id']
