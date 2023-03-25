from utils.duriel import *
url = 'http://www.baidu.com/s?'

# data = {'wd': '我饿了'}
# res = urlencode(data)
# print(res)
# re_url = url + res
# print(re_url)
#
# print(unquote(re_url))
a = 'mtopjsonp2(asdjklj)'
r = re.findall('mtopjsonp2\((.*?)\)', a)
print(r)