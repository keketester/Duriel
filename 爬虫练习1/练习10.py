from utils.duriel import *
url = 'http://www.xinfadi.com.cn/getPriceData.html'
r = rq.post(url, headers=head).json()

for i in r['list']:
    print(i)