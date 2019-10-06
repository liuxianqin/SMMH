#codeing=utf-8

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.qq.com',80))    #AF_INET:ipv4 STREAM:TCP for stream
s.send(b'GET/HTTP/1.1\r\nHOST:www.qq.com\r\nConnection: close\r\n\r\n')

buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close()

header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))

with open('sina.html','wb') as f:
    f.write(html)

