import json
import time
from hashlib import md5
import requests
import execjs
from Crypto.PublicKey import RSA
from pyquery import PyQuery
from selenium import webdriver
import aiohttp
import aiofiles
import asyncio
import csv
import re
from bs4 import *
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Queue
from lxml import etree
import base64
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad

parser = etree.HTMLParser(encoding="utf-8")
rq = requests.session()  # 创建session对象，保持会话
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Connection': 'close'
    }
false = False
true = True


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
        return eval(msg.rstrip(b'\0') .decode('utf-8'))


class Dersa:
    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    # Encrypt message
    @classmethod
    def encrypt_rsa(cls, message, public_key):
        rsa_key = RSA.import_key(public_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        encrypted_message = cipher.encrypt(message.encode())
        return base64.b64encode(encrypted_message)

    # Decrypt message
    @classmethod
    def decrypt_rsa(cls, encrypted_message, private_key):
        rsa_key = RSA.import_key(private_key)
        cipher = PKCS1_OAEP.new(rsa_key)
        decoded_message = base64.b64decode(encrypted_message)
        return cipher.decrypt(decoded_message).decode()


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64':base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


chaojiying = Chaojiying_Client('13206769672', 'koko9999', '945818')
