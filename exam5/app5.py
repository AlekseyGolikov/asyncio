
import random
import asyncio
import time

connects = ['task1','task2','task3','task4','task5','task6','task7','task8','task9','task10']

async def execute(delay, value):
    await asyncio.sleep(delay)
    print('delay='+str(delay)+' value='+str(value))

async def main():
    """ Using asyncio.create_task() method to run coroutines concurrently as asyncio"""
    tasks = []
    for i in range(10):
        # вместо i можно использовать random.randint(1,11)
        tasks.append(asyncio.create_task(execute(i, connects[i])))

    print(tasks)

    print('started at {}'.format(time.strftime('%X')))
    start = time.perf_counter()
    # Wait until both tasks are completed (should take around 2 secs. )

    await asyncio.gather(*tasks)

    print('finished ad {}'.format(time.strftime('%X')))
    end = time.perf_counter() - start
    print(end)

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

