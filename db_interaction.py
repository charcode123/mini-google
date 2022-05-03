
class db_interaction():
    def __init__(self):
        conn = 'mongodb://localhost:27017/search-engine'
        client = mongo_client.MongoClient(conn)
        self.db = client.searchengine
        self.col = self.db.get_collection('search-engine-collection')
    def insert(self,d):
        self.col.insert_one(d)
    def get(self):
        ob = self.col.find()
        l = [item["URL"] for item in ob]
        return l