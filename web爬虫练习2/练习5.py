from utils.duriel import *
url = 'http://www.baidu.com'
prox = {'http': 'http://120.77.215.57:80'}
r = rq.get(url, headers=head, proxies=prox)
r.encoding = 'gb2312'
print(r.text)
"""
代理地址: http://www.kxdaili.com/dailiip/2/2.html
"""