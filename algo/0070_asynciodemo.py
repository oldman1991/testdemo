#! /usr/bin/env python
# -*- coding: utf-8 -*-
# create by oldman
# Date: 2019/7/23

"""
python协程
"""
import asyncio


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main(urls):
    for url in urls:
        await crawl_page(url)

# asyncio.run(main(['url_1','url_2','url_3','url_4']))


async def main2(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    for task in tasks:
        await task

# asyncio.run(main2(['url_1','url_2','url_3','url_4']))


async def main3(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)

# asyncio.run(main3(['url_1','url_2','url_3','url_4']))


async def worker_1():
    await asyncio.sleep(1)
    return 1

async def worker_2():
    await asyncio.sleep(2)
    return 2/0

async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main4():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1,task_2,task_3,return_exceptions=True)
    print(res)

asyncio.run(main4())