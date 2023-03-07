from utils.duriel import *
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

data = {"csrf_token": "",
"cursor": "-1",
"offset": "0",
"orderType": "1",
"pageNo": "1",
"pageSize": "20",
"rid": "A_PL_0_391125700",
"threadId": "A_PL_0_391125700"
        }

"""
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
        e = Math.floor(e),
        c += b.charAt(e);
    return c
}
function b(a, b) {
    var c = CryptoJS.enc.Utf8.parse(b)
      , d = CryptoJS.enc.Utf8.parse("0102030405060708")
      , e = CryptoJS.enc.Utf8.parse(a)
      , f = CryptoJS.AES.encrypt(e, c, {
        iv: d,
        mode: CryptoJS.mode.CBC
    });
    return f.toString()
}
function c(a, b, c) {
    var d, e;
    return setMaxDigits(131),
    d = new RSAKeyPair(b,"",c),
    e = encryptedString(d, a)
}
function d(d, e, f, g) {
    var h = {}
      , i = a(16);
    return h.encText = b(d, g),
    h.encText = b(h.encText, i),
    h.encSecKey = c(i, e, f),
    h
}
function e(a, b, d, e) {
    var f = {};
    return f.encText = c(a + e, b, d),
    f
}
"""

d = data
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
key = "0CoJUm6Qyw8W8jud"
key1 = "9WrkeGJvHM4DjEJa"
iv = "0102030405060708"

def get_key():
    return "b4d1a28dae8ce795a82a5f7ca5d78b353d0fdfc2f2daef04b8a93f64a6d4a84348a158e0bc687c9865642ea9a433f8b35e8fa993c7b71e11ce680e776592f028712ca7e8d508ca1c4e6f64cdedda0298b33ddc6b0871947a6eca7e13cee3c6aac53803891f5502d116087ae0af3ac603c6c9a2451e2fb1315309ff139d958ffa"


def get_params():
    f1 = Edcryp.encrypt(d, key, iv)
    f2 = Edcryp.encrypt(f1, key1, iv)
    return f2

param = get_params()
r = rq.post(url, headers=head, data={
    "params":get_params(),
    "encSecKey":get_key()
}).json()['data']['comments']
for i in r:
    try:
        print(f'评论: {i["beReplied"][0]["content"]}, 回复: {i["content"]}')
    except Exception:
        pass