import asyncio


async def task1():
    print("Task 1 Started")
    await asyncio.sleep(2)
    print("Task 1 Finished")


async def task2():
    print("Task 2 Started")
    await asyncio.sleep(1)
    print("Task 2 Finished")


async def main():
    await asyncio.gather(task1(), task2())


asyncio.run(main())