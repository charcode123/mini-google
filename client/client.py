
import socket            
import json
s = socket.socket()        
port = 12345

meth = ""
while(meth!='find' and meth!='insert'):
    meth = input("enter a valid method  (insert/find): ") 
if meth == 'insert':                 
    n = input('enter the description of the URL ')
    a = input("enter the URL ")
    if n == '' or a == '':
        d = {}
    else:
        d = {'description':n,'URL':a}
else:
    d = {}
d= json.dumps({"ob":d,"method":meth})
s.connect(('127.0.0.1', port))
s.send(d.encode())




s.close()  
