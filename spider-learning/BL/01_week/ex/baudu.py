import requests

wd = "Python"

try:
    kv = {'wd':wd}
    r = requests.get("http://www.baidu.com/s",params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("Fail")