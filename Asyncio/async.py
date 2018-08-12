import asyncio
import time
import random

def sync_run(name):
    random_int = random.randint(50000, 29384782)
    start_time = time.time()
    for i in range (0, random_int):
        pass
    elapsed_time = time.time() - start_time
    print (f'{name} with {random_int} iterations took {elapsed_time} seconds')

def run_the_sync_run():
    start_time = time.time()
    for i in range (0, 10):
        name = f'Iteration {i}'
        sync_run(name)
    elapsed_time = time.time() - start_time
    print(f'Loop iterations took {elapsed_time} seconds')

#run_the_sync_run()

async def async_run(name):
    random_int = random.randint(50000, 29384782)
    start_time = time.time()
    for i in range (0, random_int):
        pass
    elapsed_time = time.time() - start_time
    msg =  (f'{name} with {random_int} iterations took {elapsed_time} seconds')
    print (msg)
    return (msg)

def compile_async_tasks():
    tasks = []

    for i in range (0, 10):
        name = f'async iteration {i}'
        tasks.append (asyncio.ensure_future(async_run(name)))
    print(tasks)
    return tasks

tasks = compile_async_tasks()

start_time = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
elapsed_time = time.time() - start_time
print(f'async Loop iterations took {elapsed_time} seconds')