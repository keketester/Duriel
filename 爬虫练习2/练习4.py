from utils.duriel import *
url = 'https://chongqing.zbj.com/search/service?l=0&b=1&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90&r=2'
r = rq.get(url, headers=head).text
t = etree.HTML(r)
# ts = t.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div/div/a/div[2]/div[1]/div/text()')
# print(ts)
# for i in ts:[['恒易好数据工作室'], ['￥100']]
#     print(i)
ts = t.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div[1]/div')
lis = []
for i in ts:
    ts = i.xpath('./div/a/div[2]/div[1]/div/text()')
    money = i.xpath('./div/div[2]/div[1]/span/text()')
    lis.append([ts[0], money[0]])
    print(ts, money)
for i in lis:
    print(i)