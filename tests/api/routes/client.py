import unittest
from unittest.mock import patch

from orders.api.routes.client import Client


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        self.mocks = {}
        self.patches = []

        resource_patch = patch('orders.api.routes.client.Resource')
        self.mocks['resource_mock'] = resource_patch.start()
        self.patches.append(resource_patch)

        order_placement_service_patch = patch('orders.api.routes.client.OrderPlacementService')
        self.mocks['order_placement_service_mock'] = order_placement_service_patch.start()
        self.patches.append(order_placement_service_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()

    def test_post_calls_order_placement_service(self):
        # Act
        Client.post()

        # Assert
        self.mocks['order_placement_service_mock'].assert_called()
        self.mocks['order_placement_service_mock'].return_value.\
            place_order.assert_called()
