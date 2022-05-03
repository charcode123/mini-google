
import socket		
import json
import db_interaction as db


#connecting to mongodb
col=db.connect()  



# next create a socket object
s = socket.socket()		
print ("Socket successfully created")
port = 1234			
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
        db.insert(col,d)
    elif method =='find':
        results = db.get(col)
        print(results)
    c.close()

# Breaking once connection closed
    break
