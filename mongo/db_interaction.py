
import pymongo
from pymongo import MongoClient
def connect():
    client = MongoClient('localhost', 27017)
    db = client.searchengine
    col = db.get_collection('search-engine-collection')
    return col
def insert(col,d):
    col.insert_one(d)
    print("inserted")
def get(col):
    ob = col.find()
    l = [item["URL"] for item in ob]
    return l        