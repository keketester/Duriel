from utils.duriel import *
with open('1.js', 'r', encoding='utf8') as f:
    r = execjs.compile(f.read())
a = r.call('s', 'dog')
print(a)
