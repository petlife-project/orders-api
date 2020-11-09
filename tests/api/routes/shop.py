import unittest
from unittest.mock import patch

from orders.api.routes.shop import Shop


class ShopTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        resource_patch = patch('orders.api.routes.shop.Resource')
        self.mocks['resource_mock'] = resource_patch.start()
        self.patches.append(resource_patch)

        polling_service_patch = patch('orders.api.routes.shop.PollingService')
        self.mocks['polling_service_mock'] = polling_service_patch.start()
        self.patches.append(polling_service_patch)

        confirmation_service_patch = patch('orders.api.routes.shop.ConfirmationService')
        self.mocks['confirmation_service_mock'] = confirmation_service_patch.start()
        self.patches.append(confirmation_service_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_get_calls_polling_service(self):
        # Act
        Shop.get()

        # Assert
        self.mocks['polling_service_mock'].assert_called()
        self.mocks['polling_service_mock'].return_value.\
            get_orders.assert_called_with('petshop')

    def test_put_calls_cancelation_service(self):
        # Act
        Shop.put()

        # Assert
        self.mocks['confirmation_service_mock'].assert_called()
        self.mocks['confirmation_service_mock'].return_value.\
            confirm.assert_called()
