import unittest
from unittest.mock import MagicMock, patch

from orders.api.services.confirmation import ConfirmationService


# pylint: disable=protected-access
class ConfirmationServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        abort_patch = patch('orders.api.services.confirmation.abort')
        self.mocks['abort_mock'] = abort_patch.start()
        self.patches.append(abort_patch)

        parser_patch = patch('orders.api.services.confirmation.ChangeStatusParser')
        self.mocks['parser_mock'] = parser_patch.start()
        self.patches.append(parser_patch)

        mongo_patch = patch('orders.api.services.confirmation.get_mongo_adapter')
        self.mocks['mongo_mock'] = mongo_patch.start()
        self.patches.append(mongo_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_parser(self):
        # Setup
        mock_self = MagicMock()

        # Act
        ConfirmationService.__init__(mock_self)

        # Assert
        self.mocks['parser_mock'].assert_called_once()

    def test_confirm_gets_field_calls_mongo_returns_200(self):
        # Setup
        mock_self = MagicMock()

        # Act
        response = ConfirmationService.confirm(mock_self)

        # Assert
        mock_self._update_in_mongo.assert_called_once()
        self.assertEqual(response, 200)

    def test_update_in_mongo_calls_confirm_order_successfully(self):
        # Setup
        order_id = 'coxinha_frango_catupiry'

        # Act
        ConfirmationService._update_in_mongo(order_id)

        # Assert
        self.mocks['mongo_mock'].return_value.\
            confirm_order.assert_called_with('coxinha_frango_catupiry')

    def test_update_in_mongo_confirm_order_except_key_error_calls_abort(self):
        # Setup
        order_id = 'risoles_queijo'
        self.mocks['mongo_mock'].return_value.\
            confirm_order.side_effect = KeyError('Order not found')

        # Act
        ConfirmationService._update_in_mongo(order_id)

        # Assert
        self.mocks['abort_mock'].assert_called_with(404, extra="'Order not found'")
