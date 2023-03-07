import requests
import urllib3

urllib3.disable_warnings()
rq = requests.session()  # 创建session对象，保持会话
url = 'https://movie.douban.com/chart'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
r = rq.get(url=url, headers=head, verify=False)
page = r.text
print(page)
with open('baidu.html', 'w', encoding='UTF-8') as f:
    f.write(page)

