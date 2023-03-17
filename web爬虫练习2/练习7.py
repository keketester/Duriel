from utils.duriel import *


def func1(name):
    print(f'我是 {name}')
    return name


def fn(r):
    print(r.result())


with ThreadPoolExecutor(10) as t:
    for i in range(10):
        # t.submit(func1, f'线程{i}').add_done_callback(fn)
        res = t.map(func1, ['大菠萝', '巴尔', '墨菲斯托'])
for i in res:
    print(i)


# f1 = Thread(target=func1, args=(20,))
# f2 = Thread(target=func2, args=(20,))
# f1.start()
# f2.start()
# f1.join()
# f2.join()







