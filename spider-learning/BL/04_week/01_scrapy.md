# scrapy

功能强大的爬虫框架

INSTALL:`pip install scrapy`



5+2  

。。。

Downloader Middleware  修改、丢弃、新增请求或者响应

Spider Middleware    	修改、丢弃、新增请求或者爬取项



### CMD

startproject 

genspider 创建一个爬虫

settings 获得配置信息

crawl 运行一个爬虫

list

shell 启动URL调试命令行



CMD可以方便的执行自动化脚本





### 目录结构

```shell
user@carbon:~/Desktop/BL/04_week/demo$ tree
.
├── demo				
│   ├── __init__.py				#初始化脚本
│   ├── items.py				#继承类
│   ├── middlewares.py			
│   ├── pipelines.py			#继承类
│   ├── __pycache__
│   ├── settings.py				#配置文件
│   └── spiders
│       ├── __init__.py
│       └── __pycache__
└── scrapy.cfg            #部署爬虫 放到服务器上 对本机使用不需要修改

4 directories, 7 files

```

```python
# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['python123.io']
    start_urls = ['http://python123.io/']

    def parse(self, response):
        pass

```



```python
# 关键字 yield
# 生成器  不断产生值的函数   产生一个值  被冻结 再次被唤醒    值是一样的
# 节省存储空间 使用灵活 
```





### Request对象

.url 

.method

.headers

.body

.meta 用户添加的拓展信息 

.copy()    复制这个请求



### Response

.url

.status  200

.headers

.body

.flags

.request

.copy()







## 提取信息的方法

Beautiful Soup

re

lxml

Xpath Selector

CSS Selector



```css
<HTML>.css('a::attr(href)').extract()
			#标签名称 标签属性
```





