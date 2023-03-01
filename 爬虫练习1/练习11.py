from utils.duriel import *
url = 'https://movie.douban.com/chart'
r = rq.get(url, headers=head).text
res = BeautifulSoup(r, 'html.parser')
r1 = res.find_all(class_='nbg')
print(r1)
r2 = []
for i in r1:
    r2.append(str(i).split('"'))

for i in r2:
    print(i[5])
