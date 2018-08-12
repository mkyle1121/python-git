import random
import asyncio

async def co(id):

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(co(i)))

    await asyncio.gather(*tasks)
