import unittest
from unittest.mock import MagicMock, patch

from orders.api.services.polling import PollingService


# pylint: disable=protected-access
class PollingServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        re_patch = patch('orders.api.services.polling.re')
        self.mocks['re_mock'] = re_patch.start()
        self.patches.append(re_patch)

        abort_patch = patch('orders.api.services.polling.abort')
        self.mocks['abort_mock'] = abort_patch.start()
        self.patches.append(abort_patch)

        jsonify_patch = patch('orders.api.services.polling.jsonify')
        self.mocks['jsonify_mock'] = jsonify_patch.start()
        self.patches.append(jsonify_patch)

        parser_patch = patch('orders.api.services.polling.PollingParser')
        self.mocks['parser_mock'] = parser_patch.start()
        self.patches.append(parser_patch)

        mongo_patch = patch('orders.api.services.polling.get_mongo_adapter')
        self.mocks['mongo_mock'] = mongo_patch.start()
        self.patches.append(mongo_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_parser(self):
        # Setup
        mock_self = MagicMock()

        # Act
        PollingService.__init__(mock_self)

        # Assert
        self.mocks['parser_mock'].assert_called_once()

    def test_get_orders_calls_methods_returns_all_orders(self):
        # Setup
        mock_self = MagicMock(parser=MagicMock(field='test123'))
        type_ = 'client'

        # Act
        result = PollingService.get_orders(mock_self, type_)

        # Assert
        mock_self._check_forbidden_characters.assert_called()
        self.mocks['mongo_mock'].return_value.\
            search.assert_called_with({'client.username': 'test123'})
        self.assertEqual(result, self.mocks['jsonify_mock'].return_value)

    def test_get_orders_no_results_excepts_key_error_calls_abort(self):
        # Setup
        mock_self = MagicMock(parser=MagicMock(field='test123'))
        type_ = 'test'
        self.mocks['mongo_mock'].return_value.search.side_effect = KeyError('No orders found')

        # Act
        PollingService.get_orders(mock_self, type_)

        # Assert
        self.mocks['abort_mock'].assert_called_with(404, extra="'No orders found'")

    def test_check_forbidden_characters_matches_calls_abort(self):
        # Setup
        input_mock = 'test'
        self.mocks['re_mock'].match.return_value = True

        # Act
        PollingService._check_forbidden_characters(input_mock)

        # Assert
        self.mocks['abort_mock'].assert_called_with(403, extra='Invalid username')
