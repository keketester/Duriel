from utils.duriel import *
s = '我的电话：10010你的电话：10086'


@reckon_time
def a():
    phone = re.findall(r'\d+', s)
    print(phone)


@reckon_time
def b():
    phone1 = re.finditer(r'\d+', s)  # finditer 返回迭代器，效率比findall高
    print(phone1)
# p = []
# for i in phone1:
#     print(i.group())
#     p.append(i.group())
# print(p)


rq = requests.session()  # 创建session对象，保持会话
url = 'https://movie.douban.com/chart'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/86.0.4240.198 Safari/537.36'}
r = rq.get(url, headers=head)  # 发起请求
page = r.text  # 获取源码

obj = re.compile(
    r'subject/\d+/"  title="(.*?)">.*?<span class="rating_nums">(.*?)</span>',
    re.S)


@reckon_time
def c():
    t1 = obj.findall(page)
    for i in t1:
        print(i)


@reckon_time
def d():
    t2 = obj.finditer(page)
    for i in t2:
        print(i.groups())


c()
d()
