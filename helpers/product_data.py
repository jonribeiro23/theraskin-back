from flask_restful import reqparse

product = reqparse.RequestParser()


product.add_argument('composition',
                          type=str,
                          required=True)
product.add_argument('descript',
                          type=str,
                          required=True)
product.add_argument('ean',
                          type=str,
                          required=True)
product.add_argument('name',
                          type=str,
                          required=True)
product.add_argument('use',
                          type=str,
                          required=True)
product.add_argument('review_link',
                          type=str,
                          required=True)
