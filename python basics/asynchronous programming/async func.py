import asyncio

async def main():
    print(100)
    await other()

    print(200)

async def other():
    print(1)
    await asyncio.sleep(2)
    print(2)

asyncio.run(main())