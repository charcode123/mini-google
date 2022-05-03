import pymongo
from pymongo import mongo_client
import socket		
import json	

def insert(col,val):
    col.insert_one(val)

def get(col):
    ob = col.find()
    l = [item["name"] for item in ob]
    return l

conn = 'mongodb://localhost:27017/search-engine'
client = mongo_client.MongoClient(conn)
db = client.searchengine
col = db.get_collection('search-engine-collection')
# col.insert_one({'name':'test', 'age':'20'})
# ob = col.find()
# for item in ob:
#     print(item)


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
    print(col)
    method = d['method']
    d = d['ob']
    if method =='insert':
        insert(col,d)
        print('inserted')
    elif method =='find':
        results = get(col)
        print(results)
    c.close()

# Breaking once connection closed
    break
