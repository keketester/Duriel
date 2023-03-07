from utils.duriel import *


def func1(name):
    print(name)


with ThreadPoolExecutor(10) as t:
    for i in range(100):
        t.submit(func1, f'线程{i}')


# f1 = Thread(target=func1, args=(20,))
# f2 = Thread(target=func2, args=(20,))
# f1.start()
# f2.start()
# f1.join()
# f2.join()







