#coding=utf-8
import time
import threading
import socket
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    #to_say=input('服务器:')
    sock.send(b'Welcome!')
    while True:
        to_say=input('服务器：')
        data=sock.recv(1024)
        print(data.decode('utf-8')) 
        if not data or data.decode('utf-8')=='exit':
            break
        #sock.send(('Hello,%s!' %data.decode('utf-8')).encode('utf-8'))
        sock.send((to_say.encode('utf-8')))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection...')

while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
