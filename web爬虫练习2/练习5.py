from utils.duriel import *
url = 'http://www.baidu.com/'
prox = {'http': 'http://180.184.49.178:80'}
r = rq.get(url, headers=head, proxies=prox)
print(r.text)
"""
代理地址: http://www.kxdaili.com/dailiip/2/2.html
"""