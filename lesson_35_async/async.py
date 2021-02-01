from time import time
import os
import asyncio
import aiohttp
import aiofiles
import requests

URL = 'https://api.pushshift.io/reddit/comment/search'
FILE = '../comments.json'

time_per_user = dict()
author_list = [
    'SweetReptile',
    'toofarbyfar',
    'ImAnonymous135',
    'crescentcactus',
    'AdelineKraxx',
    'toofarbyfar',
    'ImAnonymous135',
    'crescentcactus',
    'AdelineKraxx',
    'toofarbyfar',
    'ImAnonymous135',
    'crescentcactus',
    'AdelineKraxx',
    'toofarbyfar',
    'ImAnonymous135',
    'crescentcactus',
    'AdelineKraxx',
    'bradg2415'
]
loop = asyncio.get_event_loop()


async def proceed_author(author):
    async with aiohttp.TCPConnector(ssl=False, loop=loop) as connector:
        params = {'size': 500, 'author': author, 'fields': ('author', 'body', 'created_utc')}
        async with aiohttp.ClientSession(loop=loop, connector=connector) as session:
            async with session.get(URL, params=params) as response:
                start_time = time()
                data = await response.text()
                time_per_user[params["author"]] = time() - start_time


async def main():
    await asyncio.gather(
        *[proceed_author(author) for author in author_list]
    )

if __name__ == '__main__':
    start = time()
    loop.run_until_complete(main())
    loop.close()
    for k, v in time_per_user.items():
        print(v, k)
    print(f'Took {time() - start}')
