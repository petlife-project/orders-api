import unittest
from unittest.mock import MagicMock, patch

from orders.api.services.order_placement import OrderPlacementService


# pylint: disable=protected-access
class OrderPlacementServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        parser_patch = patch(
            'orders.api.services.order_placement.OrderPlacementParser')
        self.mocks['parser_mock'] = parser_patch.start()
        self.patches.append(parser_patch)

        mongo_patch = patch(
            'orders.api.services.order_placement.get_mongo_adapter')
        self.mocks['mongo_mock'] = mongo_patch.start()
        self.patches.append(mongo_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_parser(self):
        # Setup
        mock_self = MagicMock()

        # Act
        OrderPlacementService.__init__(mock_self)

        # Assert
        self.mocks['parser_mock'].assert_called_once()

    def test_place_order_calls_methods_returns_200(self):
        # Setup
        mock_self = MagicMock()

        # Act
        response = OrderPlacementService.place_order(mock_self)

        # Assert
        self.assertEqual(response, 200)

    def test_resolve_request_fields_successfull_run_alters_dict(self):
        # Setup
        doc = {
            'petshop_username': 'petshop_username123',
            'petshop_name': 'petshop_name123',
            'service_id': 'service_id123',
            'service_name': 'service_name123',
            'client_username': 'client_username123',
            'client_name': 'client_name123',
            'client_pet': {'tchunay': {'species': 'dog'}},
            'schedule_datetime': '2020-10-11-09-30'
        }

        # Act
        OrderPlacementService._resolve_request_fields(doc)

        # Assert
        self.assertEqual(doc, {
            'petshop': {
                'username': 'petshop_username123',
                'name': 'petshop_name123'
            },
            'service': {
                'id': 'service_id123',
                'name': 'service_name123'
            },
            'client': {
                'username': 'client_username123',
                'name': 'client_name123',
                'pet': {'tchunay': {'species': 'dog'}}
            },
            'schedule': {
                'datetime': '2020-10-11-09-30'
            }
        })

    def test_create_control_fields_alters_doc(self):
        # Setup
        doc = {}

        # Act
        OrderPlacementService._create_control_fields(doc)

        # Assert
        self.assertEqual(doc, {
            'status': {
                'confirmed': False,
                'cancelled': False,
                'rejected': False
            }
        })

    def test_insert_in_mongo_calls_place_order_mongo_method(self):
        # Setup
        doc = {}

        # Act
        OrderPlacementService._insert_in_mongo(doc)

        # Assert
        self.mocks['mongo_mock'].return_value.place_order.assert_called_with({})
