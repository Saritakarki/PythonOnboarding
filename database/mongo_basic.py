from pymongo import MongoClient


class MongoConnect:

    def __init__(self):

        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['testDb']

    def insert_in_database(self, col, data):
        self.db[col].insert_one(data)

    def insert_many_in_database(self, col , data):
        self.db[col].insert_many(data)

    def delete_from_database(self, col, data):
        self.db[col].delete_one(data)

    def get_all(self, col):
        res = self.db[col].find()
        print(res)

    def get_from_database(self, col, query):
        res = self.db[col].find(query)
        print(res)

    def update_one_in_database(self,col, query, up_data):
        res = self.db[col].update_one(query, {'$set': up_data})
        if res:
            print(True)


if __name__ == '__main__':
    test = MongoConnect()
    test.insert_in_database('test', {"name": "sarita", "address": "pokhara"})
    test.delete_from_database('test', {"name": "sarita", "address": "pokhara"})
    test.get_all('test')
    test.get_from_database('test', {"name": "sarita", "address": "pokhara"})
    test.update_one_in_database('test', {"name": "asasas"}, {"name":"asmita"})
