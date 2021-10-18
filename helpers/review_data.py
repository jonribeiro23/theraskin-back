from flask_restful import reqparse

review_args = reqparse.RequestParser()


review_args.add_argument('review_link',
                          type=str,
                          required=True)
