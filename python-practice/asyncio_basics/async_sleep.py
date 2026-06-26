import asyncio


async def countdown():

    for i in range(5, 0, -1):
        print(i)
        await asyncio.sleep(1)

    print("Time's Up!")


asyncio.run(countdown())