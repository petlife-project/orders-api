import unittest
from unittest.mock import MagicMock, patch

from orders.api.services.cancellation import CancellationService


# pylint: disable=protected-access
class CancellationServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        abort_patch = patch('orders.api.services.cancellation.abort')
        self.mocks['abort_mock'] = abort_patch.start()
        self.patches.append(abort_patch)

        parser_patch = patch('orders.api.services.cancellation.ChangeStatusParser')
        self.mocks['parser_mock'] = parser_patch.start()
        self.patches.append(parser_patch)

        mongo_patch = patch('orders.api.services.cancellation.get_mongo_adapter')
        self.mocks['mongo_mock'] = mongo_patch.start()
        self.patches.append(mongo_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_parser(self):
        # Setup
        mock_self = MagicMock()

        # Act
        CancellationService.__init__(mock_self)

        # Assert
        self.mocks['parser_mock'].assert_called_once()

    def test_cancel_gets_field_calls_mongo_returns_200(self):
        # Setup
        mock_self = MagicMock(parser=MagicMock(field='coxinha_frango_catupiry'))

        # Act
        response = CancellationService.cancel(mock_self)

        # Assert
        self.mocks['mongo_mock'].return_value.\
            cancel_order.assert_called_with('coxinha_frango_catupiry')
        self.assertEqual(response, 200)

    def test_cancel_cancel_order_except_key_error_calls_abort(self):
        # Setup
        mock_self = MagicMock(parser=MagicMock(field='risoles_queijo'))
        self.mocks['mongo_mock'].return_value.\
            cancel_order.side_effect = KeyError('Order not found')

        # Act
        CancellationService.cancel(mock_self)

        # Assert
        self.mocks['abort_mock'].assert_called_with(404, extra="'Order not found'")
