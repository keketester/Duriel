# Example usage
import asyncio

from utils.duriel import *
# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# data = {'a': 123, 's': '22', 'name': '向可'}
# data = json.dumps(data)
# data = 'askjfhahkasd案达成阿达开始了打开了asdasdasda'
# data = {'a':11, 'name': '向可', 'phone': '13206732822'}
# s = Edcryp.encrypt(json.dumps(data), 'sad87yhgft67yhuj')
# s = Aes.enc(data, 'sad87yhgft67yhuj')
#
# print(s)
# s = Aes.dec(s, 'sad87yhgft67yhuj')
# print(s)
# print(type(s))


# data = 'askjfhahkasd案达成阿达开始了打开了asdasdasda'
# s = Des.enc(data, 'sad87yhg')
# data = {'a':11, 'name': '向可', 'phone': '13206732822'}
# s = Des.enc(json.dumps(data), 'sad87yhg')
#
# print(s)
# s = Des.dec(s, 'sad87yhg')
# print(s)
a = 5
b = 10
b = a+b
a = b-a
b = b-a
print(a, b)
# print(Rsa.public_key)
# print(Rsa.private_key)
s = 'rsa加密啥会计法开始减肥黄金卡'
enc = Rsa.enc(s, Rsa.public_key)
print(enc)
dec = Rsa.dec(enc, Rsa.private_key)
print(dec)