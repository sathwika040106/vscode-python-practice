import asyncio
import time


async def timer():

    start = time.time()

    await asyncio.sleep(3)

    end = time.time()

    print(f"Completed in {end - start:.2f} seconds")


asyncio.run(timer())