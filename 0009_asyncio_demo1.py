# coding=utf-8
# create by oldman at 2018/1/9
import asyncio


async def computer(x, y):
    print("Compute {} + {}".format(x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await computer(x, y)
    print("{} + {} = {}".format(x, y, result))


print_sum(3, 5)
