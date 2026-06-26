import asyncio


async def student(name):

    print(f"{name} started exam")

    await asyncio.sleep(2)

    print(f"{name} completed exam")


async def main():

    await asyncio.gather(
        student("Sathwika"),
        student("Rahul"),
        student("Priya")
    )


asyncio.run(main())