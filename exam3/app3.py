
import asyncio
import time

async def execute(i, delay, value):
    await asyncio.sleep(delay)
    print(value)
    return str(i)

async def main():
    print('started at {}'.format(time.strftime('%X')))
    res1 = await execute(1, 1, 'hello')
    res2 = await execute(2, 2, 'world')
    print('finished ad {}'.format(time.strftime('%X')))
    print(res1+' '+res2)

asyncio.run(main())
