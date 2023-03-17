import execjs
from utils.duriel import *
print(execjs.get().name)
r = execjs.eval("""
    '巴尔_墨菲斯托_迪亚波罗'.split('_')
""")
print(r)

js = """
    function fn(a,b){
        return a+b;
    }
"""
r = execjs.compile(js)
res = r.call('fn', 10, 11)
print(res)
