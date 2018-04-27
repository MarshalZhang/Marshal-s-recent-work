# client
import socket

s = socket.socket();
host = '172.17.134.132';
port = 8080;
s.connect((host, port));
while True:
    rec = s.recv(1024);
    if rec:
        print('from server',(host,port));
        print('receive: ',rec.decode());
    d = input('send to server:');
    s.send(d.encode());
    if d== '-1':
        break

s.close();

