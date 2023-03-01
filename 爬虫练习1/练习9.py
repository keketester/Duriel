from utils.duriel import *
url = 'https://www.dy2018.com/'
r = rq.get(url, headers=head).content.decode('gb2312')
print(type(r))