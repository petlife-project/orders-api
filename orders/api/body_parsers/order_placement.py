from flask_restful import reqparse


class OrderPlacementParser:
    """ Parser for the placing of an order, every field is required.
    """
    def __init__(self):
        self._fields = [
            {'name': 'petshop_username', 'type': str, 'location': 'json', 'required': True},
            {'name': 'petshop_name', 'type': str, 'location': 'json', 'required': True},

            {'name': 'service_id', 'type': str, 'location': 'json', 'required': True},
            {'name': 'service_name', 'type': str, 'location': 'json', 'required': True},

            {'name': 'client_username', 'type': str, 'location': 'json', 'required': True},
            {'name': 'client_name', 'type': str, 'location': 'json', 'required': True},
            {'name': 'client_pet', 'type': dict, 'location': 'json', 'required': True},

            {'name': 'schedule_datetime', 'type': str, 'location': 'json', 'required': True}
        ]

        self.parser = self._create_parser()
        self.fields = self.parser.parse_args()

    def _create_parser(self):
        parser = reqparse.RequestParser()
        for field in self._fields:
            parser.add_argument(**field)
        return parser
