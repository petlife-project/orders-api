import os

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from cheroot.wsgi import PathInfoDispatcher
from cheroot.wsgi import Server as WSGIServer

from orders.api.routes.client import Client
from orders.api.routes.shop import Shop

from orders.utils.env_vars import JWT_ALGORITHM, JWT_PRIVATE_PEM, JWT_PUBLIC_PEM

APP = Flask(__name__)
APP.config['JWT_ALGORITHM'] = JWT_ALGORITHM
APP.config['JWT_PUBLIC_KEY'] = JWT_PUBLIC_PEM
JWTManager(APP)

CORS(APP)
API = Api(APP)
PORT = int(os.getenv('PORT', '8080'))

DISPATCHER = PathInfoDispatcher({'/': APP})
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

API.add_resource(Client, '/client')
API.add_resource(Shop, '/shop')

if __name__ == '__main__':
    print(f'Server running on port {PORT}')
    SERVER.safe_start()
