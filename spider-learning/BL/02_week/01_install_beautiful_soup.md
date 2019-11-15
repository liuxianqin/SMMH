# bs4

https://python123.io/ws/demo.html

```python
>>> r = requests.get('https://python123.io/ws/demo.html')
>>> demo = r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(demo, "html.parser")
>>> print(soup.prettify())
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
>>> 

```

解析、建立、维护 标签树的功能库

Name名称 成对出现

属性 Attribute 0个或多个 





## 解析器

lxml                              pip install lxml

xml                                pip install lxml

html5lib                          pip install html5lib



## 基本元素

soup.tag 获得标签



Tag                 		<></>

Name					<tag>.name

Attribute				<tag>.attrds

NavigableString    <tag>.string

Comment    注释



### 参照demo

```Python
>>> soup.title
<title>This is a python demo page</title>

>>> tag = soup.a   #只能获取到第一个
>>> tag
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>

>>> tag.name
'a'
>>> tag.parent.name
'p'
>>> tag.parent.parent.name
'body'

>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
>>> tag.attrs['href']
'http://www.icourse163.org/course/BIT-268001'

>>> type(tag.attrs)
<class 'dict'>
>>> type(tag)
<class 'bs4.element.Tag'>

>>> tag.string              #可以跨越多个标签层次到最里面
'Basic Python'


```



