import unittest
from unittest.mock import MagicMock, patch

from orders.utils.db.mongo_adapter import MongoAdapter, PyMongoError


# pylint: disable=protected-access
class MongoAdapterTestCase(unittest.TestCase):

    def setUp(self):
        self.patches = []
        self.mocks = {}

        mongo_client_patch = patch('orders.utils.db.mongo_adapter.MongoClient')
        self.mocks['mongo_client_mock'] = mongo_client_patch.start()
        self.patches.append(mongo_client_patch)

        mongo_conn_patch = patch('orders.utils.db.mongo_adapter.MONGO_CONNECTION_STRING',
                                 new='test_conn_string')
        self.mocks['mongo_conn_mock'] = mongo_conn_patch.start()
        self.patches.append(mongo_conn_patch)

        orders_col_patch = patch('orders.utils.db.mongo_adapter.ORDERS_COLLECTION',
                                 new='test_orders_string')
        self.mocks['orders_col_mock'] = orders_col_patch.start()
        self.patches.append(orders_col_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_init_creates_client(self):
        # Setup
        mock_self = MagicMock()

        #  Act
        MongoAdapter.__init__(mock_self)

        # Assert
        self.mocks['mongo_client_mock'].assert_called_with(
            'test_conn_string',
            connect=True
        )
        self.assertEqual(
            mock_self.db_,
            self.mocks['mongo_client_mock'].return_value.petlife['test_orders_string']
        )

    @staticmethod
    def test_place_order_successful_run_returns_nothing():
        # Setup
        mock_self = MagicMock()
        doc = {'test': 'order'}

        # Act
        MongoAdapter.place_order(mock_self, doc)

        # Assert
        mock_self.db_.insert_one.assert_called_with({'test': 'order'})

    def test_create_unexpected_error_raises_runtime_error(self):
        # Setup
        mock_self = MagicMock()
        mock_self.db_.insert_one.side_effect = PyMongoError()
        doc = {}

        # Act & Assert
        with self.assertRaises(RuntimeError):
            MongoAdapter.place_order(mock_self, doc)
