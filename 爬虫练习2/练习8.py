import time

from utils.duriel import *


async def func1():
    print('func1')
    # time.sleep(3)
    await asyncio.sleep(3)
    print('func1')


async def func2():
    print('func2')
    await asyncio.sleep(2)
    print('func2')


async def func3():
    print('func3')
    await asyncio.sleep(4)
    print('func3')


async def main():
    t = [asyncio.create_task(func1()),
         asyncio.create_task(func2()),
         asyncio.create_task(func3())]
    await asyncio.wait(t)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)


async def download(url):
    print(f'开始下载{url}')
    await asyncio.sleep(2)
    print(f'下载完成{url}')


async def main():
    url = [
        'www.baidu.com',
        'www.4399.com',
        'www.12306.com'
    ]
    lis = []
    for i in url:
        d = asyncio.create_task(download(i))
        lis.append(d)
    await asyncio.wait(lis)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)
