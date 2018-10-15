from core import *
from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Transaction(Resource):

    def get(self, tx_id):
        pass

    def put(self, tx_id):
        pass


class Block(Resource):

    def get(self, height):
        pass

    def put(self, height):
        pass


@app.route('/height')
def chain_height():
    pass


api.add_resource(Transaction, '/transaction')
api.add_resource(Block, '/block')

