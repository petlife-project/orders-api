import unittest
from unittest.mock import patch, MagicMock

from orders.api.body_parsers.change_status import ChangeStatusParser


# pylint: disable=protected-access
class ChangeStatusParserTestCase(unittest.TestCase):

    def setUp(self):
        self.patches = []
        self.mocks = {}

        flask_parser_patch = patch('orders.api.body_parsers.change_status.RequestParser')
        self.mocks['flask_parser_mock'] = flask_parser_patch.start()
        self.patches.append(flask_parser_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_parser_and_parses_args(self):
        # Setup
        mock_self = MagicMock()
        self.mocks['flask_parser_mock'].return_value.\
            parse_args.return_value = {'order_id': 'test123'}

        # Act
        ChangeStatusParser.__init__(mock_self)

        # Assert
        self.mocks['flask_parser_mock'].return_value.add_argument.assert_called()
        self.assertEqual(mock_self.field, 'test123')
