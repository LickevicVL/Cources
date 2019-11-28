import asyncio


async def replenish():
    print('Try to replenish')
    await asyncio.sleep(10)
    print('Stop replenish')


async def withdraw():
    print('Try to withdraw')
    await asyncio.sleep(3)
    print('Stop withdraw')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(func()) for func in [replenish, withdraw]]
    loop.run_until_complete(asyncio.wait(tasks))
