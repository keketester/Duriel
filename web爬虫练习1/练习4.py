from utils.duriel import *
url = 'https://fanyi.baidu.com/sug'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
rq = requests.session()
datas = {'kw': 'dog'}
r = rq.post(url, headers=head, data=datas).json()
data = get_analysis_json(eval(js(r)))
print(data)
