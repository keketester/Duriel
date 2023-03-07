from utils.duriel import *
obj = re.compile(r"""<span class="title">(.*?)</span>.*?导演: (.*?)&nbsp.*?"v:average">(.*?)</span>""", re.S)

'''爬豆瓣电影top250'''


@reckon_time
def find_all():
    result = []
    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='
        r = rq.get(url, headers=head).text
        result += obj.findall(r)
        print(f'执行中，倒计时: {9-i}')
        time.sleep(3)
    result.sort(key=lambda j: j[2], reverse=True)
    with open('movie.csv', 'w', newline="", encoding='utf8') as f:
        csvwrite = csv.writer(f)
        csvwrite.writerow(['电影名', '导演', '评分'])
        for k in result:
            csvwrite.writerow(k)
            print(k)


@reckon_time
def find_iter():
    res = []
    for i in range(10):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='
        r = rq.get(url, headers=head).text
        result = obj.finditer(r)
        for j in result:
            res.append(j.groups())
        print(f'执行中，倒计时: {9 - i}')
        time.sleep(3)
    res.sort(key=lambda k: k[2], reverse=True)
    with open('movie1.csv', 'w', newline="", encoding='utf8') as f:
        csvwrite = csv.writer(f)
        csvwrite.writerow(['电影名', '导演', '评分'])
        for k in res:
            csvwrite.writerow(k)
            print(k)


# find_all()
find_iter()
