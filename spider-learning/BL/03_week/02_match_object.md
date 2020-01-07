# match 对象



```python
>>> match = re.search(r'[1-9]\d{5}','BIT 100081')
>>> 
>>> match.group(0)
'100081'
>>> type(match)
<class 're.Match'>

```

## match 对象的属性

.string  文本

.re         pattern对象 正则表达式

.pos  开始位置

.endpos 结束位置



## match对象的常用方法

.group(0) 获得匹配后的字符串

.start()

.end()

.span()  返回(.start(),.end())



```python
>>> match.group(0)
'100081'
>>> type(match)
<class 're.Match'>
>>> m.string
'100081 BIT 100084TSU'
>>> m.re
re.compile('[1-9]\\d{5}')
>>> m.pos
0
>>> m.endpos
20
>>> 
>>> m.pos
0
>>> m.endpos
20
>>> m.group()
'100084'
>>> m.group(0)
'100084'
>>> m.end()
17
>>> m.start()
11
>>> m.span()
(11, 17)
>>> 


```





### 贪婪  re库的默认匹配方式  找到最长的

最小匹配

*?

+?

??

{m.n}?



