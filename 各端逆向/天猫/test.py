"""
************************************天猫逆向sign************************************
line:445
https://g.alicdn.com/mtb/lib-mtop/2.6.1/mtop.js:formatted
sign: j
j = h(d.token + "&" + i + "&" + g + "&" + c.data)

需要参数: 
h方法
d.token
i
g
c.data
"""
import time
from utils.duriel import *
import execjs

t = int(round(time.time() * 1000))
# i = (new Date).getTime()  当前毫秒Unix时间戳
# g = c.appKey || ("waptest" === d.subDomain ? "4272" : "12574478")
# g = '12574478'
# d.token = '81323998d31aa5446ec30801f529ce3f' cookie里面_m_h5_tk的值
# d.token
a = '53c181d7eb419bf8cbf6281ad8c36b6c'
# i
i = t
# g
g = '12574478'
# c.data
id = '567286481283'
# data1 = '{"id":"'
# data2 = f'{id}","detail_v":"3.3.2","exParams":"'
# data3 = '{\"ali_refid\":\"a3_430673_1006:1606610177:N:bxNI9asMVP/AOCjH1ACKaQ==:cb6d425ec0a2ec6f7af420ce5a2d8aef\",\"ali_trackid\":\"1_cb6d425ec0a2ec6f7af420ce5a2d8aef\",\"id\":\"567286481283\",\"skuId\":\"4862740755533\",\"spm\":\"a2e0b.20350158.31919782.1\",\"queryParams\":\"ali_refid=a3_430673_1006%3A1606610177%3AN%3AbxNI9asMVP%2FAOCjH1ACKaQ%3D%3D%3Acb6d425ec0a2ec6f7af420ce5a2d8aef&ali_trackid=1_cb6d425ec0a2ec6f7af420ce5a2d8aef&id=567286481283&skuId=4862740755533&spm=a2e0b.20350158.31919782.1\",\"domain\":\"https://chaoshi.detail.tmall.com\",\"path_name\":\"/item.htm\"}"}'
# d = data1+data2+data3
data = '%7B%22id%22%3A%22567286481283%22%2C%22detail_v%22%3A%223.3.2%22%2C%22exParams%22%3A%22%7B%5C%22ali_refid%5C%22%3A%5C%22a3_430673_1006%3A1606610177%3AN%3AbxNI9asMVP%2FAOCjH1ACKaQ%3D%3D%3A325c66cbe93b46c68a88a0015a70f720%5C%22%2C%5C%22ali_trackid%5C%22%3A%5C%221_325c66cbe93b46c68a88a0015a70f720%5C%22%2C%5C%22id%5C%22%3A%5C%22567286481283%5C%22%2C%5C%22skuId%5C%22%3A%5C%224862740755533%5C%22%2C%5C%22spm%5C%22%3A%5C%22a2e0b.20350158.31919782.1%5C%22%2C%5C%22queryParams%5C%22%3A%5C%22ali_refid%3Da3_430673_1006%253A1606610177%253AN%253AbxNI9asMVP%252FAOCjH1ACKaQ%253D%253D%253A325c66cbe93b46c68a88a0015a70f720%26ali_trackid%3D1_325c66cbe93b46c68a88a0015a70f720%26id%3D567286481283%26skuId%3D4862740755533%26spm%3Da2e0b.20350158.31919782.1%5C%22%2C%5C%22domain%5C%22%3A%5C%22https%3A%2F%2Fchaoshi.detail.tmall.com%5C%22%2C%5C%22path_name%5C%22%3A%5C%22%2Fitem.htm%5C%22%7D%22%7D'

with open('tianmao.js', 'r', encoding='utf8') as f:
    r = execjs.compile(f.read())
res = r.call('h', a+"&"+str(i)+"&"+g+"&"+data)
print(res)
# par = f'?jsv=2.6.1&appKey=12574478&t={i}&sign={res}&api=mtop.taobao.pcdetail.data.get&v=1.0&isSec=0&ecode=0' \
#       f'&timeout=10000&dataType=json&valueType=string&ttid=2022@taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true' \
#       f'&preventFallback=true&type=json&data={d}'
head['cookie'] = 't=d901ef26c2afa509a52c4d8103daa5f0; lid=t_1516706636221_0161; _tb_token_=e0addebeb336; cookie2=1a2478ca7a817833e54d1b9a96b49cbd; xlly_s=1; dnk=t_1516706636221_0161; uc1=existShop=false&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie14=UoezRmAO4aF0MQ%3D%3D&pas=0&cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D; uc3=nk2=F6k3HS2g4UgmYlRaL5gKeMNpOm0%3D&vt3=F8dCsfTwuffvPz6AG1I%3D&id2=UU6oKtge%2B2wFqA%3D%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=t_1516706636221_0161; _l_g_=Ug%3D%3D; uc4=id4=0%40U2xlpFcZDLj%2F2En3pcIGnirh33Pi&nk4=0%40FbMocxjds8rFjJ4sqtYk8cOPaN627Jk9S4rHwEbn5w%3D%3D; unb=2693628663; lgc=t_1516706636221_0161; cookie1=B0ehhxVc5l0D%2BvtoMiTUbuNvgy4EwVUwT1um6CZo01c%3D; login=true; cookie17=UU6oKtge%2B2wFqA%3D%3D; _nk_=t_1516706636221_0161; sgcookie=E100EG3IOIxshIxb0zvfAXg6HQ9QyEIkJGa2bOOUUU1i%2FWY0HvXZgGUJhXxd68HX9QzipSBZtwZZ3%2FIORuUVLSD54P8d6It36dLxLH5LyShtWdsNzDqrg4j7a0nrHCehuXaJ; cancelledSubSites=empty; sg=13e; csg=2dffbcff; cna=mwSkHJBiG0MCAQ5ojnGvG1Vr; x5sec=7b22617365727665723b32223a226237373363373563346635326230636665306633303830643463396362366561434b6d39394b4147454d4c5970374b776e637a446e774561444449324f544d324d6a67324e6a4d374d7967434d506d33684d594351414d3d227d; _m_h5_tk=c2da6f3f1b82de262e6e63adf51e76fe_1679637710190; _m_h5_tk_enc=fb12de3e8c9a039adb26726b89e1ef84; isg=BJKST6yMIjDYwF5LM8rNvWoD41h0o5Y9Bc6MOFzr9cUwbzJpRDNJTLzO38vTPg7V; l=fBNQbUoeNPooeyKiBOfZPurza77TxIRAIuPzaNbMi9fPOV5M52_GW1MIRR8HCnGVFsgXR37vCcaaBeYBq_C-nxvtUR-DrwHmne_7Qn5..; tfstk=cV6PBdidK8ey9jSLWKvFu3y0HFGRa48H5x-wZyQzOIH0K4Kk7s0sJnA-Ln-UFFdl.'

ur = f'https://h5api.m.tmall.com/h5/mtop.taobao.pcdetail.data.get/1.0/?jsv=2.6.1&appKey=12574478&t=1679630551504&sign=b727622ea7ad4ceea611a6df4d74175e&api=mtop.taobao.pcdetail.data.get&v=1.0&isSec=0&ecode=0&timeout=10000&dataType=json&valueType=string&ttid=2022%40taobao_litepc_9.17.0&AntiFlood=true&AntiCreep=true&preventFallback=true&type=json&data=' + data
r = rq.get(ur, headers=head).json()
print(r)
