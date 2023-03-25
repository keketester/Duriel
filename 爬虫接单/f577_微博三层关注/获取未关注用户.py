from utils.duriel import *
first = []
sed = []
name = '阿司匹林42195米'
start = time.time()
head['cookie']='XSRF-TOKEN=vkqkkvTFv8iGhsVydWwEvFkN; _s_tentry=weibo.com; Apache=1633592923976.2747.1679541574513; SINAGLOBAL=1633592923976.2747.1679541574513; ULV=1679541574543:1:1:1:1633592923976.2747.1679541574513:; login_sid_t=54fc9548196c74b626f3fc56774d6676; cross_origin_proto=SSL; wb_view_log=1536*8641.25; PC_TOKEN=334ede8bc1; SSOLoginState=1679559272; SUB=_2A25JGHrdDeRhGeBI71EY8SrEzDyIHXVqbOsVrDV8PUNbmtAbLVXtkW9NRpz5GmGcwGs9IMQbps7UwN5LqtQfDEq_; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhAGTnShGc22d_qvWGG9hdu5JpX5KzhUgL.FoqcShe4eKBRS052dJLoIpW1xH98-.UiH.HH-h.7eh.N; ALF=1711095306; WBPSESS=Dt2hbAUaXfkVprjyrAZT_G0LJtzkybNujAhy8oS0mf6Q5_CYKHMRTF41bVNOJvkp0mf2dWdK1umMwuaPo7geWwjdfCT8-ewlCkTXUpg4UAj-1Q77AIdfwA9Sz32qm64G9vqKbAjwMBgv415o2aRmv6Tlt_FMdMRjuO5riw-STtBt5IaySHiQ0mfACPnzcuOCcGg8S9OwoL-BYgIunFfmnA=='


def down1():
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
        try:
            time.sleep(1)
            print(f'监测第 {k+1} 个用户是否需要关注')
            friends_url = f'https://weibo.com/ajax/friendships/friends?page=1&uid={j[1]}'  # 获取当前用户关注用户列表
            r = rq.get(friends_url, headers=head).json()['users']
        except:
            with open('需要关注.txt', 'a', encoding='utf8') as f:
                f.write(f'{j[2]},  {j[1]}\n')


if __name__ == '__main__':
    down1()
    down2()
    print(f'耗时: {time.time()-start}')
