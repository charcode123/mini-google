
import socket            
import json
s = socket.socket()        
 
port = 12345               
n = input('enter the name')
a = input("enter the age ")
if n == '' or a == '':
    d = {}
else:
    d = {'name':n,'age':a}
meth = ""
while(meth!='find' and meth!='insert'):
    meth = input("enter a valid method")


s.connect(('127.0.0.1', port))
d= json.dumps({"ob":d,"method":meth})
s.send(d.encode())

s.close()  