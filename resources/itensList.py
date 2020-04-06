from flask_restful import Resource
from models.item import ItemModel


class ItensList(Resource):

    def get(self):
        return {'itens': [item.json() for item in ItemModel.query.all()]}
