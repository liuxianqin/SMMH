

# requests库

```python
r.status_code 

r.text  #响应内容的字符串形式

r.encoding #从HTTP header中猜测是内容编码方式

r.apparent_encoding #从内容分析出的编码方式

r.content #HTTP响应内容的二进制形式


```

当header中不存在charset，默认ISO-8859-1

