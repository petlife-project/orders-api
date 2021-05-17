from flask_restful import reqparse


def parse_req():
    fields = [
        {'name': 'petshop_username', 'type': str, 'location': 'json', 'required': True},
        {'name': 'petshop_name', 'type': str, 'location': 'json', 'required': True},

        {'name': 'service_id', 'type': str, 'location': 'json', 'required': True},
        {'name': 'service_name', 'type': str, 'location': 'json', 'required': True},

        {'name': 'client_username', 'type': str, 'location': 'json', 'required': True},
        {'name': 'client_name', 'type': str, 'location': 'json', 'required': True},
        {'name': 'client_pet', 'type': dict, 'location': 'json', 'required': True},

        {'name': 'schedule_datetime', 'type': str, 'location': 'json', 'required': True}
    ]

    parser = reqparse.RequestParser()

    for field in fields:
        parser.add_argument(**field)

    return parser.parse_args()
