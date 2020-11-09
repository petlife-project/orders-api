from flask_restful.reqparse import RequestParser


class PollingParser:
    """ Parser for the polling service,
        getting the username of the sender
    """
    def __init__(self):
        parser = RequestParser()
        parser.add_argument(
            name='username',
            type=str,
            location='args',
            required=True
        )
        self.field = parser.parse_args()['username']
