#coding=utf-8

import time
locatime = time.strftime("%Y-%m-%d" )
report = file('report.html')
line = []
for i in report.readlines():
    line.append(i)
report.close()
line.insert(7,'<p>\n    <a href="report %s .html" target="_blank">test %s</a>\n</p>\n '%(locatime，localtime))
s = ''.join(line)
reportnew = file('report.html', 'w')
reportnew.write(s)
reportnew.close()

