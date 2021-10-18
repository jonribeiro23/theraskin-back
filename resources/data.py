from flask_restful import Resource
from pprint import pprint
from models.db import DB

class SaveProduct(Resource):
    def post(self):
        from helpers.product_data import product
        db = DB()
        data = product.parse_args()
        if db.save_product_data(data):
            return {'msg': 'ok'}, 201
        return {'msg': 'err'}, 500


class GetInfo(Resource):
    def get(self, ean):
        db = DB()
        data = db.get_product(ean)

        if data:
            return {'msg': 'ok', 'data': data}, 200
        return {'msg': 'err'}, 500


class HandleReview(Resource):
    def get(self, ean):
        db = DB()
        data = db.get_review(ean)
        if data:
            return {'msg': 'ok', 'data': data}, 200
        return {'msg': 'err'}, 500

    def post(self, ean):
        from helpers.review_data import review_args
        from helpers.reviews import Reviews

        review = Reviews()
        data = review_args.parse_args()
        comments = review.get_review(data['review_link'])
        db = DB()
        if db.save_review(comments, ean):
            return {'msg': 'ok'}, 201
        return {'msg': 'err'}, 500



class Test(Resource):
    def get(self):
        return {'msg': 'test'}
