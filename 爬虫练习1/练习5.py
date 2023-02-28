import requests
from utils.duriel import *

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=30'

rq = requests.session()
r = rq.get(url, headers=head).json()

r.sort(key=lambda i: i['rating'][0],  reverse=True)
with open('movies.txt', 'w', encoding='utf8') as f:
    for i in r:
        f.write(str(i)+'\n')
        print(i)
