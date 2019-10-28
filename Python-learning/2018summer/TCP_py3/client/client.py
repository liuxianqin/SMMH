#coding=utf-8

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999))

print(s.recv(1024).decode('utf-8'))
while(1):
    data=input('客户端:')
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
