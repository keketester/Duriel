from utils.duriel import *

urls = []


async def download(url):
    name = url.rsplit('/', 1)[1]
    async with aiohttp.ClientSession() as aios:
        async with aios.get(url) as aiores:
            with open(f'pics/{name}') as f:
                f.write(await aiores.content.read())


async def main():
    ts = []
    for i in urls:
        ts.append(asyncio.create_task(download(i)))
    await asyncio.wait(ts)


if __name__ == '__main__':
    asyncio.run(main())