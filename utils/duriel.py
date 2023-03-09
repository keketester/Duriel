import json
import time
import requests
from selenium import webdriver
import aiohttp
import aiofiles
import asyncio
import csv
import re
from bs4 import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

parser = etree.HTMLParser(encoding="utf-8")
rq = requests.session()  # 创建session对象，保持会话
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Connection': 'close'
    }
false = False
true = True
options = webdriver.ChromeOptions()
# options设置chrome位置
options.binary_location = r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
# 配置到实例
driver = webdriver.Chrome(chrome_options=options)


def js(r):
    """
    转换json格式
    :param r: 需要转换的数据
    :return: json格式
    """
    s = json.dumps(
        r,
        ensure_ascii=False,
        sort_keys=True,
        indent=4,
        separators=(
            ',',
            ':'))
    return s


def list_trans_dict(s):
    """
    将列表参数转换成字典
    :param s: 列表参数
    :return: 返回字典
    """
    data = {}
    for i in range(int(len(s) / 2)):
        data[s[::2][i]] = s[1::2][i]
    return data


def analysis_json(indict, pre=None):
    """
    递归查询json数据key、value
    :param indict:
    :param pre:
    :return:
    """
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in analysis_json(value, pre):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in analysis_json(v, pre):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in analysis_json(v, pre):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


def get_analysis_json(indict):
    """
    将analysis_json返回值整理成一个列表数据
    :param indict:
    :return:
    """
    data = analysis_json(indict)
    lis = []
    for i, j in enumerate(data):
        lis += [j[0], j[1]]
    return lis


def reckon_time(func):  # func 被装饰的函数名称
    def inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)  # 调用被装饰的函数
        print(f'耗时: {(time.time()-start):.20f}')
        return res  # 返回被装饰函数运行结果
    return inner


# AES加解密
class Edcryp():

    @classmethod
    def encrypt(cls, data, key, iv, mode=AES.MODE_CBC):
        crypto = AES.new(key.encode('utf8'), mode, iv.encode('utf8'))
        msg = crypto.encrypt(pad(json.dumps(data).encode('utf-8'), 16))
        return base64.b64encode(msg).decode('utf-8')

    @classmethod
    def decrypt(cls, data, key, iv, mode=AES.MODE_CBC):
        decrypto = AES.new(key.encode('utf8'), mode, iv.encode('utf8'))
        msg = decrypto.decrypt(base64.b64decode(data.encode('utf-8')))
        return eval(msg.strip().decode('utf-8'))
