import os

from flask import Flask
from flask_restful import Api

from cheroot.wsgi import PathInfoDispatcher
from cheroot.wsgi import Server as WSGIServer

from orders.api.routes.client_orders import ClientOrders
from orders.api.routes.shop_orders import ShopOrders

APP = Flask(__name__)
API = Api(APP)
PORT = int(os.getenv('PORT', '8080'))

DISPATCHER = PathInfoDispatcher({'/': APP})
SERVER = WSGIServer(('0.0.0.0', PORT), DISPATCHER)

API.add_resource(ClientOrders, '/client_orders')
API.add_resource(ShopOrders, '/shop_orders')

if __name__ == '__main__':
    SERVER.safe_start()
