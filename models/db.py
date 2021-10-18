import pymongo
class DB:
    def __init__(self):
        self.cluster = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.cluster['theraskin']

    def save_product_data(self, data: dict) -> bool:
        try:
            if self.exist(data['ean']):
                return True

            self.db['product'].insert(data)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def save_review(self, data: dict, ean: str) -> bool:
        try:
            for item in data:
                item['ean'] = ean
                self.db['reviews'].insert(item)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def get_product(self, ean: str) -> list:
        try:
            res = [self._format_product(x) for x in self.db['product'].find({'ean': ean})]
        except Exception as e:
            print(e)
            return None
        else:
            return res

    def get_review(self, ean: str) -> list:
        try:
            res = [self._format_review(x) for x in self.db['reviews'].find({'ean': ean})]
        except Exception as e:
            print(e)
            return None
        else:
            return res

    def exist(self, ean: str) -> int:
        return self.db['product'].find({'ean': ean}).count()

    def _format_product(self, data) -> dict:
        return {
            "composition": data['composition'],
            "descript": data['descript'],
            "ean": data['ean'],
            "name": data['name'],
            "use": data['use'],
            "review_link": data['review_link']
        }

    def _format_review(self, data) -> dict:
        return {
            "comment": data['comment']
        }