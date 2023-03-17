# Example usage
import asyncio

from utils.duriel import *
# Import necessary libraries
import requests
from bs4 import BeautifulSoup


async def f1(r):
    if r >= 5 and r <= 10:
        await asyncio.sleep(r-4)
        print(f'r>=5, 停{r-4}S')
    if r >= 11:
        await asyncio.sleep(r-4)
        print(f'r>=10, 停{r-4}S')
    print(r)


async def main():
    t = []
    for i in range(20):
        t.append(asyncio.create_task(f1(i)))
    await asyncio.wait(t)

if __name__ == '__main__':
    asyncio.run(main())
