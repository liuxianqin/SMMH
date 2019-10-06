import urllib.request

def load_data():
    url="http://www.baidu.com/"
    responce=urllib.request.urlopen(url)
    print(responce)
    data=responce.read()
    print(data.decode('utf-8'))

    with open('baidu.html','w',encoding='utf-8') as f:
        f.write(data.decode('utf-8'))


load_data()
