#http://ip138.com/ips138.asp?ip=10.30.1.1

import requests

IPaddress = "120.77.37.192"
url = "http://ip138.com/ips138.asp?ip="

try:
    r = requests.get(url+IPaddress)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:-500])
except:
    print("Fail")
