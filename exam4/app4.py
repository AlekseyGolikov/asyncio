

import asyncio
import time

async def execute(i, delay, value):
    await asyncio.sleep(delay)
    # print('function {} started at {}'.format(i, time.strftime('%X')))
    print(value)
    return i

async def main():
    """ Using asyncio.create_task() method to run coroutines concurrently as asyncio"""

    task1 = asyncio.create_task(execute(1, 1, 'hello'))
    task2 = asyncio.create_task(execute(2, 2, 'world'))

    print('started at {}'.format(time.strftime('%X')))
    # Wait until both tasks are completed (should take around 2 secs. )
    res1 = await task1
    res2 = await task2
    print('finished ad {}'.format(time.strftime('%X')))

asyncio.run(main())

