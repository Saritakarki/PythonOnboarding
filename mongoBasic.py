from pymongo import MongoClient


class MongoConnect:
    global db
    client = MongoClient('mongodb://localhost:27017/')
    db = client['testDb']

    def insertInDatabase(self, col, data):
        db[col].insert_one(data)

    def deleteFromDatabase(self, col, data):
        db[col].delete_one(data)

    def getAll(self, col):
        res = db[col].find()
        print(res)

    def getFromDatabase(self, col, query):
        res = db[col].find(query)
        print(res)

    def updateOneInDatabase(self,col, query, up_data):
        res = db[col].update_one(query, {'$set': up_data})
        if res:
            print(True)


if __name__ == '__main__':
    test = MongoConnect()
    test.insertInDatabase('test', {"name": "sarita", "address": "pokhara"})
    test.deleteFromDatabase('test', {"name": "sarita", "address": "pokhara"})
    test.getAll('test')
    test.getFromDatabase('test', {"name": "sarita", "address": "pokhara"})
    test.updateOneInDatabase('test', {"name": "asasas"}, {"name":"asmita"})
