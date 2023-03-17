import time

from utils.duriel import *


def func1(q):
    for i in range(20):
        q.put(i)
        print(f'{i} 被放入队列')
    q.put('没了')


def func2(q):
    while 1:
        a = q.get()
        if a == '没了':
            break
        print(a)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=func1, args=(q,))
    p2 = Process(target=func2, args=(q,))
    p1.start()
    p2.start()
    print(q)
