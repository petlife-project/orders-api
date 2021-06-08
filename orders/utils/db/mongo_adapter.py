from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from orders.utils.env_vars import MONGO_CONNECTION_STRING, ORDERS_COLLECTION


class MongoAdapter:
    """ Wrapper for connecting with Mongo DB and doing operations.
    """
    def __init__(self):
        self.client = MongoClient(
            MONGO_CONNECTION_STRING,
            connect=True
        )
        self.db_ = self.client.petlife[ORDERS_COLLECTION]

    def place_order(self, doc):
        """ Creates a document on set collection

            Args:
                doc (dict): The document being inserted

            Raises:
                RuntimeError: If anything unexpected happens during the operation
        """
        try:
            self.db_.insert_one(doc)
            return
        except PyMongoError as error:
            raise RuntimeError('Unexpected error when working with MongoDB.') from error

    def search(self, query):
        """ Uses the query provided to fetch the orders related to that user.

            Args:
                query (dict): The search term, matching the username to the provided input

            Raises:
                KeyError: If no orders are found for that user.

            Returns:
                results (list): List of orders, already filtered from Mongo Results Object
        """
        results = list(self.db_.find(query))

        if not results:
            raise KeyError('No orders related to this user')

        for doc in results:
            doc['_id'] = str(doc['_id'])

        return results

    def cancel_order(self, order_id, user):
        """ Queries the database via the _id index and updates the value
            of the cancelled field inside the status object

            Args:
                order_id (str): The id of the order to be cancelled.

            Raises:
                KeyError: If no orders match the searched id.
        """
        username = user['username']
        type_ = user['type']
        query = {'_id': ObjectId(order_id), f'{type_}.username': username}
        change = {'$set': {'status.cancelled': True}}

        update = self.db_.find_one_and_update(query, change)

        if not update:
            raise KeyError('No orders found with provided id')

    def confirm_order(self, order_id, user):
        """ Queries the database via the _id index and updates the value
            of the confirmed field inside the status object

            Args:
                order_id (str): The id of the order to be confirmed.

            Raises:
                KeyError: If no orders match the searched id.
        """
        username = user['username']
        type_ = user['type']
        query = {'_id': ObjectId(order_id), f'{type_}.username': username}
        change = {'$set': {'status.confirmed': True}}

        update = self.db_.find_one_and_update(query, change)

        if not update:
            raise KeyError('No orders found with provided id')

    def reject_order(self, order_id, user):
        """ Queries the database via the _id index and updates the value
            of the rejected field inside the status object

            Args:
                order_id (str): The id of the order to be rejected.

            Raises:
                KeyError: If no orders match the searched id.
        """
        username = user['username']
        type_ = user['type']
        query = {'_id': ObjectId(order_id), f'{type_}.username': username}
        change = {'$set': {'status.rejected': True}}

        update = self.db_.find_one_and_update(query, change)

        if not update:
            raise KeyError('No orders found with provided id')
