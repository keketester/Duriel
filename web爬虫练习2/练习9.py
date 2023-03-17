from utils.duriel import *

urls = ["https://img.tt98.com/d/file/pic/20180531112817968/5aa1f381bae72.jpg",
        "https://img2.baidu.com/it/u=1624316916,4062419783&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=889",
        "https://img2.baidu.com/it/u=3455294109,1337782831&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500"]


async def download(url):
    name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as aios:
        async with aios.get(url) as aiores:
            content = await aiores.content.read()
            with open(f'pics/{name}', 'wb') as f:
                f.write(content)
                print('保存成功')


async def main():
    ts = []
    for i in urls:
        ts.append(asyncio.create_task(download(i)))
    await asyncio.wait(ts)


if __name__ == '__main__':
    # asyncio.run(main())
    for i, j in enumerate(urls):
        r = rq.get(j)
        with open(f'pics/{i}.jpeg', 'wb') as f:
            f.write(r.content)
            print('保存成功')
