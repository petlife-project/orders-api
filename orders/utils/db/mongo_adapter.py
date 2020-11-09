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
