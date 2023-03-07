from urllib.request import urlopen
url = 'http://www.baidu.com'
res = urlopen(url)
data = res.read().decode('utf-8')
print(data)

with open("baidu.html", mode='w', encoding='utf8') as f:
    f.write(data)
