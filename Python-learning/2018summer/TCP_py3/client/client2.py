#coding=utf-8

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('120.77.37.192',9999))

print(s.recv(1024).decode('utf-8'))
for data in [b'micjael',b'Teacy',b'Sarah',b'A',b'B',b'C']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
