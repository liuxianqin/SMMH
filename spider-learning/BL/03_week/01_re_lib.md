# Re

regular expression



ex:

PY,PYY,PYYY,PYYYYY...                                              PY+

通用的字符串表达框架 



# re.compile()

```python
regex = re.compile(pattern,flags=0)
```





# grammer



.  任何单个字符

[] 字符集

[^] 

\*    *之前的字符0次无限次拓展           abc\*       表示 ab abc abcc abccc

\+    1次或无限次拓展                             abc+        表示 abc abcc  abccc

？  0次或1次拓展                                   abc？  表示ab abc

|  或者

{m}   拓展前一个字符m次                     ab{2}c 表示 abbc

{m,n}          形式有{:4}

^ $

\d   [0-9]

\w [A-Za-z0-9_]



### 经典的正则表达式

^[A-Za-z]+$  由26个字母组成的字符串

^[A-Za-z0-9]$

^-?\d+$        整数

[1-9]\d{5}    内地邮政编码

[\\u4e00-\\u9fa5]   中文字符





### 构造方法

以IP地址例子

\d+.\d+.\d+.\d+



\d{1,3}.\d{1,3}.\d{1,3}.\d{1.3}



0-99    		[1-9]?\d

100-199 	1\d{2}

200-249	  2[0-4]\d

250-255      25[0-5]

0.0.0.1

试一试

( ([1-9]\d) | (1\d{2}) | (2[0-4]\d) | (25[0-5]) . ) {3} ( ([1-9]\d) | (1\d{2}) | (2[0-4]\d) | (25[0-5]) )



```python

>>> ip = re.search(r'( ([1-9]\d) | (1\d{2}) | (2[0-4]\d) | (25[0-5]) . ) {3} ( ([1-9]\d) | (1\d{2}) | (2[0-4]\d) | (25[0-5]) )','10.30.0.8')
>>> ip.group()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

>>> ip.group(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'

    >>> #原因：中文括号  不是的 中文括号长得很难看 一眼就看出来了
    
    >>> ##最后的原因  正则表达式不包含空格
>>> ip = re.search(r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])','10.30.30.2')
>>> ip.group(0)
'10.30.30.2'
>>> ip = re.search(r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])','120.77.37.192')
>>> ip.group(0)
'120.77.37'
>>> ip = re.search(r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])','0.0.0.1')
>>> ip.group(0)
'0.0.0.1'
>>> ip = re.search(r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])','155.155.155.155')
>>> ip.group(0)
'155.155'
>>> ip = re.findall(r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])','155.155.155.155')
>>> ip
[('15', '1', '5'), ('15', '1', '5')]

# 仍然不可以

```



try again:

0-99   [1-9]?\d

100-199    1\d{2}

200-249     2[0-4]\d

250-255     25[0-5]

 ( ([1-9]?\d | 1\d{2} |  2[0-4]\d  | 25[0-5]). ){3}([1-9]?\d | 1\d{2} |  2[0-4]\d  | 25[0-5])

 ( ([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]). ){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])





## Re 库

raw string  原生字符串类型    不包含转移符的字符串

r'[1-9]\d{5}'

使用普通的string类型表达正则会麻烦  要转义



### 方法

```python
re.search(pattern,string,flags=0)     

# re.I  re.IGNORECASE 
# re.M  re.MULTILINE   匹配每一行^
# re.S  re.DOTALL 可以匹配换行符.


re.match()

re.findall()

re.split(pattern,string,maxsplit=0,flags=0)
#maxsplit 最大分割数 

re.finditer()

re.sub()

```



```python
#re.search()
>>> import re
>>> match = re.search(r'[1-9]\d{5}','BIT 100081')
>>> match.group(0)
'100081'
>>> 

```

```python
# re.mach()
>>> match = re.match(r'[1-9]\d{5}','BIT 100081')
>>> match.group(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'group'
>>> 
>>> match = re.match(r'[1-9]\d{5}','100081 BIT')
>>> match.group(0)
'100081'
>>> 
```

```python
#re.findall()
>>> ls = re.findall(r'[1-9]\d{5}','100081 BIT 100084TSU')
>>> ls
['100081', '100084']
>>> 

```

```python
#re.split()
>>> ls = re.split(r'[1-9]\d{5}','100081 BIT 100084TSU')
>>> ls
['', ' BIT ', 'TSU']
>>> ls = re.split(r'[1-9]\d{5}','100081 BIT 100084TSU',maxsplit=1)
>>> ls
['', ' BIT 100084TSU']

```

```python
#re.finditer()
>>> for m in re.finditer(r'[1-9]\d{5}','100081 BIT 100084TSU'):
...     if m:
...             print(m.group(0))
... 
100081
100084
>>>
```

```python
#re.sub()
>>> ls = re.sub(r'[1-9]\d{5}','zipcode','100081 BIT 100084TSU')
>>> ls
'zipcode BIT zipcodeTSU'
>>> 

```



