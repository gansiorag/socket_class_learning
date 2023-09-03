import asyncio
import time

async def say_hello(delay, what):
    print('Input  ', what)
    await asyncio.sleep(delay)
    print(what, delay)

async def say_after(delay, what):
    print('Input  ', what)
    await asyncio.sleep(delay)
    print(what, delay)
    
async def main():
    print(f"started at {time.strftime('%X')}")

    task1 = asyncio.create_task(say_after(3, 'hello'))
    task2 = asyncio.create_task(say_after(1, 'world'))
    
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

cc = main()
asyncio.run(cc)
print('the end')
# ioloop = asyncio.get_event_loop()
# tasks = [ioloop.create_task(say_after(3, 'hello')), ioloop.create_task(say_after(1, 'world'))]
# wait_tasks = asyncio.wait(tasks)
# ioloop.run_until_complete(wait_tasks)
# ioloop.close()