import requests


kv = {'user-agent':'Mozilla/5.0'}
r = requests.get("https://www.amazon.cn/dp/B01FWK5H96",headers=kv)

print(r.status_code)
r.encoding = r.apparent_encoding
print(r.text)
#  <div class="a-box-inner">
#                 <i class="a-icon a-icon-alert"></i>
#                 <h4>请输入您在下方看到的字符</h4>
#                 <p class="a-last">抱歉，我们只是想确认一下当前访问者并非自动程序。为了达到最佳效果，请确保您浏览器上的 Cookie 已启用。</p>
#                 </div>
#             </div>
print(r.request.headers)
#{'User-Agent': 'python-requests/2.21.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

