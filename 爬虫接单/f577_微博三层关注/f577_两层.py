import time

from utils.duriel import *
first = []
sed = []
name = '阿司匹林42195米'
start = time.time()


def down1():
    head["cookie"] = 'XSRF-TOKEN=vkqkkvTFv8iGhsVydWwEvFkN; _s_tentry=weibo.com; Apache=1633592923976.2747.1679541574513; SINAGLOBAL=1633592923976.2747.1679541574513; ULV=1679541574543:1:1:1:1633592923976.2747.1679541574513:; login_sid_t=54fc9548196c74b626f3fc56774d6676; cross_origin_proto=SSL; wb_view_log=1536*8641.25; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFWS6MXZInGDukLyfLwbvLC5JpX5o275NHD95QcehepSKnXSKBNWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNSo50eK-RSh-XS7tt; SSOLoginState=1679541967; SUB=_2A25JH7dcDeRhGeBO6FMU-CrJzzuIHXVqbK-UrDV8PUNbmtANLRXGkW9NSgMw1HnZO78qEoJgvmW-36OU94ha1Hs1; ALF=1711078026; PC_TOKEN=975f764e89; WBPSESS=K2SXoFx4g66FRDwfdKwvLWMnFmmb1qEAu7aTbAU3NvjeZJaklITiwI3VIwiLQoBU4XGyPpf7DRno-3bUh6M-kz2f-NhkR-qRey_RBE6Xl9pid7gmRaAm40a6st3OQaWsHf8NT0ncOZqKXVrNhLTRLA=='
    fri_count = 'https://weibo.com/ajax/profile/info?uid=6335428789'  # 获取当前用户关注数量作为分页
    print(f'--------------开始获取第一个用户的第一层关注--------------')
    r = rq.get(fri_count, headers=head).json()['data']['user']['friends_count']
    fri_page = r//20 + 1
    print(f'--------------第一个用户的关注数量: {r}, 页数: {fri_page}--------------')
    for i in range(fri_page):
        time.sleep(1)
        print(f'-------开始获取第 {i+1} 个用户的第一层关注第 {i+1} 页用户--------')
        friends_url = f'https://weibo.com/ajax/friendships/friends?page={i+1}&uid=6335428789'  # 获取当前用户关注用户列表
        r = rq.get(friends_url, headers=head)
        for i in r.json()['users']:
            first.append((name, i['idstr'], i['name']))


def down2():
    for k, j in enumerate(first):
        fri_count = f'https://weibo.com/ajax/profile/info?uid={j[1]}'  # 获取当前用户关注数量作为分页
        print(f'-------总用户数: {len(first)}, 目前第 {k+1} 个用户')
        r = rq.get(fri_count, headers=head).json()['data']['user']['friends_count']
        fri_page = r//20 + 1
        for i in range(fri_page):
            time.sleep(1)
            print(f'-------第 {i+1} 页用户--------')
            friends_url = f'https://weibo.com/ajax/friendships/friends?page={i+1}&uid={j[1]}'  # 获取当前用户关注用户列表
            r = rq.get(friends_url, headers=head)
            with open(f'data/{name}.csv', 'a', newline="", encoding='utf8') as f:
                csvwrite = csv.writer(f)
                for n in r.json()['users']:
                    csvwrite.writerow([j[0], j[2], n['name']])


if __name__ == '__main__':
    down1()
    down2()
    print(f'耗时: {time.time()-start}')
