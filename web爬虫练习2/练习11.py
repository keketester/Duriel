from utils.duriel import *
from selenium import webdriver


def merge_ts():
    # mac:cat 1.ts 2.ts 3.ts > xxx.mp4
    # windows: copy /b 1.ts+2.ts+3.ts xxx.mp4
    pass


a = ['qwe.ts', 'zxcz.ts', 'cdf.ts', 'aszxc.ts']
b = ' + '.join(a)
print(b)