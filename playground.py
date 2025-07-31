import asyncio


async def fun1():
    print("fun1")


async def main():
    print("hi")
    await asyncio.sleep(2)
    await fun1()


if __name__== "__main__":
    asyncio.run(main())