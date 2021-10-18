from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.data import SaveProduct, GetInfo, Test, HandleReview


app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
app.secret_key = 'node.js'
api = Api(app)

jwt = JWTManager(app)  # /auth


# Course
api.add_resource(SaveProduct, '/save-product')
api.add_resource(HandleReview, '/review/<string:ean>')

api.add_resource(GetInfo, '/product/<string:ean>')
api.add_resource(Test, '/test')



if __name__ == '__main__':
    app.run(port=5000)
