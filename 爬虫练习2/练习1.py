import os

from utils.duriel import *
host = 'https://www.umei.cc'
url = 'https://www.umei.cc/bizhitupian/weimeibizhi/'
r = rq.get(url, headers=head).content.decode('utf-8')
res = BeautifulSoup(r, 'html.parser')
r1 = res.find('div', class_='item_list infinite_scroll').find_all("a")
lis = []
for i in r1:
    lis.append(host+i.get('href'))
se = set(lis)
# os.mkdir('pics')
for i, j in enumerate(se):
    r = rq.get(j, headers=head).content.decode('utf8')
    res = BeautifulSoup(r, 'html.parser')
    link = res.find('div', class_='big-pic').find('img')['src']
    r = rq.get(link).content
    print(f'开始下载: {link}')
    with open(f'pics/{i+1}.png', 'wb') as f:
        f.write(r)
