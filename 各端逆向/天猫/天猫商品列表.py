import json
import os.path

from utils.duriel import *
url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
a = input('请输入你要获取的商品名字: ')
kw = {'keyword': a}
key = urlencode(kw)
p = input('你想下载多少页的数据: ')
head['cookie'] = 'cna=mwSkHJBiG0MCAQ5ojnGvG1Vr; xlly_s=1; t=65079ab10fdd7d99c4d9273c34fd752c; sgcookie=E100VMzDN05jgbWVWbFUSrXNPEneoaMAuaNvFsUCenvLaYwCU10Y4%2F084d61h24n0eqc5m5dOTXNPkGKuHd7jnm6lgG0L82689jW3j%2BWL72GEfq8c2H7I9XJfNVZzhTOyLA3; uc3=vt3=F8dCsfTwuxcBz%2Fa3vrc%3D&id2=UU6oKtge%2B2wFqA%3D%3D&nk2=F6k3HS2g4UgmYlRaL5gKeMNpOm0%3D&lg2=UtASsssmOIJ0bQ%3D%3D; lgc=t_1516706636221_0161; uc4=id4=0%40U2xlpFcZDLj%2F2En3pcIGniyqCYJz&nk4=0%40FbMocxjds8rFjJ4sqtYk8cOPaN627Jk9S4rBB2VJ0A%3D%3D; tracknick=t_1516706636221_0161; _cc_=Vq8l%2BKCLiw%3D%3D; mt=ci=25_1; thw=cn; cookie2=2a4caed68bc043742d31bb345ca953f3; _tb_token_=e36beee3db731; _samesite_flag_=true; v=0; _m_h5_tk=17774cdf807b038577b1b899e554c0fa_1679724630630; _m_h5_tk_enc=495c7eabbdced300e3b78e0c945e24fa; tfstk=c2kcBmwqVjPXPmptPqwXLWCRe6RdZWR4lAkrU3e5sKOQWPMPiQ5PTuC2qrdEQ11..; l=fBglu1CmTdh2I5a6BOfZPurza77T7IRAguPzaNbMi9fPOYCH5o_NW1MUbNYMCnGVFsY9R37vCcaaBeYBqI2jPGKnNSVsrmDmnmOk-Wf..; isg=BKKiG44IMuP8USnU_AbRlS_G8ygE86YNlZ6caOw70JXAv0I51ICgHcU57_tDrx6l'
token = "17774cdf807b038577b1b899e554c0fa"
g = "12574478"
for page in range(int(p)):

    i = int(round(time.time() * 1000))
    data = '{"pNum":' + str(page) + ',"pSize":"60","refpid":"mm_26632258_3504122_32538762","variableMap":"{\\"q\\":\\"'\
           +key+'\\",\\"navigator\\":false,\\"clk1\\":\\"be7528c1151de41e8e4449c6390731be\\",\\"union_lens\\":\\"recoveryid:201_33.5.38.198_12178477_1679709979509;prepvid:201_33.51.94.81_12188292_1679711617287\\",\\"recoveryId\\":\\"201_33.8.41.104_12197299_1679711738222\\"}","qieId":"36308","spm":"a2e0b.20350158.31919782","app_pvid":"201_33.8.41.104_12197299_1679711738222","ctm":"spm-url:a2e0b.20350158.search.1;page_url:https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26' \
       + key + \
       '%26clk1%3Dbe7528c1151de41e8e4449c6390731be%26upsId%3Dbe7528c1151de41e8e4449c6390731be%26spm%3Da2e0b.20350158.search.1%26pid%3Dmm_26632258_3504122_32538762%26union_lens%3Drecoveryid%253A201_33.5.38.198_12178477_1679709979509%253Bprepvid%253A201_33.51.94.81_12188292_1679711617287"}'
    signkey = f'{token}&{i}&{g}&'+data
    with open('tianmao.js', 'r', encoding='utf-8') as f:
        jscall = f.read()
    ctx = execjs.compile(jscall).call('h',signkey)

    payload = {'jsv': '2.6.1', 'appKey': g, 't': i, 'sign': ctx, 'v': '1.0', 'type': 'jsonp',
               'timeout': 10000, 'api': 'mtop.alimama.union.xt.en.api.entry', 'dataType': 'jsonp',
                'AntiFlood': 'true', 'AntiCreep': 'true', 'callback': 'mtopjsonp2', 'data': data
               }
    res = requests.get(url, headers=head, params=payload)

    rec = re.compile('mtopjsonp2\((.*?),"ret":\["SUCCESS::调用成功"],"v":"1.0"', re.S)
    res = rec.findall(res.text)[0] + '}'

    jsondata = json.loads(res)
    print(f'*********************************开始下载第{page+1}页数据*********************************')
    if os.path.exists(f'天猫商品/{a}.csv'):
        with open(f'天猫商品/{a}.csv', 'a', encoding='utf8', newline='') as f:
            wt = csv.writer(f)
            for i in jsondata['data']['recommend']['resultList']:
                wt.writerow([i['itemName'], i['shopTitle'], i['monthSellCount'], i['realPostFee'],
                             i['pic'], i['provcity'], i['url'], i['promotionPrice'], i['sellerNickName'], i['price'],
                             i['creativeTitle']])
    else:
        with open(f'天猫商品/{a}.csv', 'a', encoding='utf8', newline='') as f:
            wt = csv.writer(f)
            wt.writerow(['商品名字', '店铺标题', '月销量', '实际减免金额', '商品图片', '发货地', '商品链接', '促销价', '卖家昵称', '价格', '创造性标题'])
            for i in jsondata['data']['recommend']['resultList']:
                wt.writerow([i['itemName'], i['shopTitle'], i['monthSellCount'], i['realPostFee'],
                             i['pic'], i['provcity'], i['url'], i['promotionPrice'], i['sellerNickName'], i['price'], i['creativeTitle']])
