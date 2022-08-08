
import random
import asyncio
import time

def timer(func):
    async def wrapper():
        start = time.perf_counter()
        f = await func()
        end = time.perf_counter() - start
        print('It takes {} secs'.format(end))
        return f
    return wrapper

connects = ['task1','task2','task3','task4']

async def execute(delay, value):
    await asyncio.sleep(delay)
    print('delay='+str(delay)+' value='+str(value))

@timer
async def main():
    tasks = []
    for i, connect in enumerate(connects):
        # вместо i можно использовать random.randint(1,11)
        tasks.append(asyncio.create_task(execute(i, connect)))
    await asyncio.gather(*tasks)

while True:
    asyncio.run(main())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

