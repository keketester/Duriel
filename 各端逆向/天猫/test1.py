import execjs
import js2py
from utils.duriel import *
a = input('请输入你要获取的商品名字: ')
kw = {'keyword': a}
key = urlencode(kw)