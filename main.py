import subprocess
import asyncio


async def main():
    tasks = [
        asyncio.create_task(subprocess.run("server.py", shell=True)),
        asyncio.create_task(subprocess.run("bot.py", shell=True)),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
