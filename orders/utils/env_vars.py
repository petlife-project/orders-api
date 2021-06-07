import os

from orders.utils.security import load_private_key, load_public_key


# MongoDB
MONGO_CONNECTION_STRING = str(os.environ.get('MONGO_CONNECTION_STRING'))
ORDERS_COLLECTION = str(os.environ.get('MONGO_ORDERS_COLLECTION'))

# JWT
JWT_PRIVATE_PEM = load_private_key()
JWT_PUBLIC_PEM = load_public_key()
JWT_ALGORITHM = 'RS256'
