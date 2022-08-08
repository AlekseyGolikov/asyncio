
import random
import asyncio
import time

connects = ['task1','task2','task3','task4','task5','task6','task7','task8','task9','task10']

def execute(delay, value):
    time.sleep(delay)
    print('delay='+str(delay)+' value='+str(value))

def main():
    """ Using asyncio.create_task() method to run coroutines concurrently as asyncio"""



start = time.perf_counter()
# Wait until both tasks are completed (should take around 2 secs. )
for i in range(10):
    execute(i, connects[i])

end = time.perf_counter() - start
print(end)

main()
