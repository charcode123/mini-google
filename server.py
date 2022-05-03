
import socket		
import json	
import pymongo
from pymongo import mongo_client
# import db_interaction as db


conn = 'mongodb://localhost:27017/search-engine'
client = mongo_client.MongoClient(conn)
db = client.searchengine
col = db.get_collection('search-engine-collection')
def insert(col,d):
    col.insert_one(d)
    print("inserted")
def get(col):
    ob = col.find()
    l = [item["URL"] for item in ob]
    return l    



# next create a socket object
s = socket.socket()		
print ("Socket successfully created")
port = 12345			
s.bind(('', port))		
print ("socket binded to %s" %(port))
results = ''
s.listen(5)	
print ("socket is listening")		
while True:

# Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )
    d= c.recv(1024).decode()
    d = json.loads(d)
    method = d['method']
    d = d['ob']
    if method =='insert':
        insert(col,d)
    elif method =='find':
        results = get(col)
        print(results)
    c.close()

# Breaking once connection closed
    break
