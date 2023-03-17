import asyncio
import time

from Crypto.Cipher import AES
from utils.duriel import Edcryp
# a = '电话是'
# b = ['我的','13213131']
# print(a.join(b))
# from utils.duriel import head
# c = {'a':'1'}
# head.update(c)
# print(head)
#
# a = 'HBWo9f1kdQw6VD5lPMnEvCkEW/GG23n5sVT+F7mNTRoq9B0QBloz4OWZRvGE6aHB0fR7TPgYNuArnLfH6l4BEIlXNlSDMCGzDE6iFbp+BSQ='
#
# b = Edcryp.decrypt(a,'QBJDsFonLaHTK20D', '0b196e85544cc8e9')
# print(b)


async def func1(r):
    print(f'func1 {r}')
    await asyncio.sleep(2)
    print('func1 end')


async def func2(r):
    print(f'func2 {r}')
    await asyncio.sleep(2)
    print('func2 end')


async def main1():
    t = []
    for i in range(4):
        t.append(asyncio.create_task(func1(i)))
    await asyncio.wait(t)


async def main2():
    t = []
    for i in range(4):
        t.append(asyncio.create_task(func2(i)))
    await asyncio.wait(t)


if __name__ == '__main__':
    asyncio.run(main1())
    asyncio.run(main2())


