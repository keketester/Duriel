import re
import requests

rq = requests.session()  # 创建session对象，保持会话
url = 'https://baijiahao.baidu.com/s?id=1721797292175421502&wfr=spider&for=pc'
r = requests.get(url=url)
page = r.text
print(page)
f1 = re.findall(r'"type":"img","link":"(.*?)?token', page)
for i in f1:
    print(i)


for i, j in enumerate(f1):
    with open(f'img/{i+1}.jpeg', 'wb') as f:
        k = j.replace('\\',"")
        r = rq.get(url=k)
        f.write(r.content)
