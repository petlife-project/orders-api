import os

from flask import Flask
from flask_restful import Api

from cheroot.wsgi import PathInfoDispatcher
from cheroot.wsgi import Server as WSGIServer

from orders.api.routes.client import Client
from orders.api.routes.shop import Shop

APP = Flask(__name__)
API = Api(APP)
PORT = int(os.getenv('PORT', '8080'))

DISPATCHER = PathInfoDispatcher({'/': APP})
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

API.add_resource(Client, '/client')
API.add_resource(Shop, '/shop')

if __name__ == '__main__':
    SERVER.safe_start()
