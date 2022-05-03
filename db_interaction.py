from pymongo import mongo_client
import pymongo
def getdb():
    conn = 'mongodb://localhost:27017/search-engine'
    client = mongo_client.MongoClient(conn)
    db = client.searchengine
    col = db.get_collection('search-engine-collection')
    col.insert_one({'name':'test', 'age':'20'})
    ob = col.find()
    for item in ob:
        print(item)
getdb()
if __name__ == '__main__':
    dbname = getdb()
    dbname[]

