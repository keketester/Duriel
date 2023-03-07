from utils.duriel import *


async def downloadxyj(cid, title):
    data = json.dumps({"book_id": "4306063500", "cid": f"4306063500|{cid}", "need_bookinfo": 1})
    url = f'http://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.request("GET", url) as aiores:
        res = await aiores.json()
        content = res['data']['novel']['content']
        async with aiofiles.open(f'xiyouji/{title}.txt', 'w', encoding='utf8') as f:
            await f.write(content)


async def get_cid():
    task = []
    url = 'http://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4306063500"}'
    r = rq.get(url, headers=head).json()
    for i in r['data']['novel']['items']:
        print(i['cid'], i['title'])
        task.append(asyncio.create_task(downloadxyj(i['cid'], i['title'])))
    await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(get_cid())
