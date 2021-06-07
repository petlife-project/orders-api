import os


# MongoDB
MONGO_CONNECTION_STRING = str(os.environ.get('MONGO_CONNECTION_STRING'))
ORDERS_COLLECTION = str(os.environ.get('MONGO_ORDERS_COLLECTION'))

# JWT
JWT_SECRET = str(os.environ.get('JWT_SECRET'))
