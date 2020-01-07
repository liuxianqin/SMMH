# Request 主要方法

## requests.request



`requests.request(method,url,**kwargs)`

method : 请求方式         r=requests.request('GET',url,**kwargs)

​										 ...

​										 r=requests.request('OPTIONS',url,**kwargs)						 获取一些参数

访问控制参数

params 字典 或者 字节序列 作为参数添加到URL中	

data 

json   JSON格式的数据

headers  字典 定制头

cookies 

auth  认证

files  字典类型

timeout 超时时间 单位s

proxies  访问代理服务器

allow_redirects   允许重定向

stream  立即下载文件

verify

cert 保存本次ssl证书路径

```Python
>>> body = 'main context'
>>> r = requests.request('POST','http://python123.io/ws,data=body)
  File "<stdin>", line 1
    r = requests.request('POST','http://python123.io/ws,data=body)
                                                                 ^
SyntaxError: EOL while scanning string literal
>>> r = requests.request('POST','http://python123.io/ws',data=body)
>>> r.text
>>> hd = {'user-agent':'Chrome/10'}
>>> r = requests.request('POST','http://python123.io/ws',headers=hd)
>>> r.text
''

>>> fs = {'file':open('data.xls','rb')}
>>> pxs = {'http':'http://user:pass@10.10.10.1:1234'
          ,'https':'https://10.10.10.1:4321'}

```

## requests.get

requests.get(url,params = None,**keargs)

params 字典或者字节流形式 











