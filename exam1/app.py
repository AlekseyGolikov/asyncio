import asyncpg
import asyncio


QUERY = '''INSERT INTO some_test_table VALUES ($1, $2, $3)'''

async def make_request(db_pool):
    # print(' делаю запрос в БД')
    await db_pool.fetch(QUERY, 1, 'string', 3)
    await asyncio.sleep(0.1)

async def main():
    tasks = []
    chunk = 200
    pended = 0

    pg_pool = await asyncpg.create_pool('postgresql://utest:utest@127.0.0.1:5432/postgres')

    for i in range(10000):
        pended += 1
        tasks.append(asyncio.create_task(make_request(pg_pool)))
        if len(tasks) == chunk or pended == 10000:
            await asyncio.gather(*tasks)
            tasks = []
            print(pended)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
